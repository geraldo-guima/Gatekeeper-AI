from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Carrega o modelo gerado
model = joblib.load('gatekeeper_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        

        hora_dia = data.get('hora_dia')
        codigo_pais = data.get('codigo_pais', 1)
        historico_logins = data.get('historico_logins', [])

        if hora_dia is None:
            return jsonify({'error': 'O campo hora_dia é obrigatório.'}), 400

        features = np.array([[hora_dia, codigo_pais]])
        prediction = model.predict(features)[0]

        falhas_recentes = sum(1 for log in historico_logins if log.get('acao_executada') == 'SENHA_INCORRETA')

        if prediction == 1 or falhas_recentes >= 2:
            risk_level = "Alto"
        else:
            risk_level = "Baixo"

        return jsonify({
            'risk_level': risk_level,
            'details': {
                'model_prediction': int(prediction),
                'failed_attempts_in_history': falhas_recentes
            }
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)