const axios = require("axios");
const dbOps = require("../dbOperations");

const AI_SERVICE_URL =
  process.env.AI_SERVICE_URL || "http://localhost:5000/predict";

/**
 * Avalia o risco do login consultando o histórico do usuário e acionando o microsserviço de IA.
 *
 * @param {Object} currentLoginData - Dados do acesso atual { horaDia, codigoPais, ipOrigem }
 * @param {number} userId - ID do usuário tentando realizar o login
 * @returns {Promise<string>} Retorna "Baixo" ou "Alto" (com fallback para "Baixo" em caso de falha)
 */
async function evaluateLoginRisk(currentLoginData, userId) {
  try {
    // 1. Busca os últimos logs de login do usuário no banco de dados
    const historicoLogins = await dbOps.getUserLoginHistory(userId, 50);

    // 2. Monta o payload completo com os dados atuais + histórico
    const payload = {
      usuario_id: userId,
      hora_dia: currentLoginData.horaDia,
      codigo_pais: currentLoginData.codigoPais,
      ip_origem: currentLoginData.ipOrigem,
      historico_logins: historicoLogins,
    };

    // 3. Faz a requisição POST para o microsserviço em Python
    const response = await axios.post(AI_SERVICE_URL, payload, {
      timeout: 3000, // Timeout de 3 segundos
    });

    return response.data.risk_level || "Baixo";
  } catch (error) {
    console.warn(
      `[AI Service Warning] Falha na comunicação com serviço de IA para o usuário ${userId}. Aplicando fallback para risco 'Baixo'. Motivo:`,
      error.message,
    );

    // Retorno seguro caso a IA esteja offline ou demore a responder
    return "Baixo";
  }
}

module.exports = {
  evaluateLoginRisk,
};
