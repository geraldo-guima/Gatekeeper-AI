# Gatekeeper AI
sistema de autenticação inteligente que avalia o nível de risco de tentativas de login em tempo real usando Aprendizado de Máquina (Árvore de Decisão) com base no contexto do acesso (horário, localização/país e histórico de tentativas)

Para o pleno funcionamento do sistema Gatekeeper AI é preciso inicializar em dois projetos distintos o gatekeeper-AI-master (aplicação de gerenciamento de logins - back e front end) e o microservicoAI (micro serviço de ia que recebe dados de login e atribui o nível de risco).

ao inicializar os dois processos é possível utilizar sua funcionalidade a partir da página web hosteada pelo localhost na gate 3000 (localhost:3000).
