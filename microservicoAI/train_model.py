import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib



# Dados sintéticos de treino cobrindo as regras de negócio:
# Features: [hora_dia (0-23), codigo_pais (1 = Brasil, 2 = Internacional)]
data = {
    'hora_dia':    [8, 10, 14, 18, 20, 2, 3, 4, 11, 15, 1, 23, 14, 3],
    'codigo_pais': [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2],
    'risco':       [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1]  # 0 = Baixo Risco, 1 = Alto Risco
}

df = pd.DataFrame(data)

X = df[['hora_dia', 'codigo_pais']]
y = df['risco']

# Treina a Árvore de Decisão
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X, y)

# Salva o modelo no arquivo .pkl
joblib.dump(clf, 'gatekeeper_model.pkl')
print("Modelo Árvore de Decisão gerado com sucesso!")