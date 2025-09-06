import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Carregar os dados
dados_brutos = pd.read_csv('smartgrid_dados_simulados.csv', index_col='Unnamed: 0', parse_dates=True)
dados_brutos.index.name = 'Data_Hora'

# Criar colunas de recursos (features)
dados_brutos['hora'] = dados_brutos.index.hour
dados_brutos['dia_da_semana'] = dados_brutos.index.dayofweek
dados_brutos['dia_do_ano'] = dados_brutos.index.dayofyear
dados_brutos['mes'] = dados_brutos.index.month

# Definir os recursos (X) e o alvo (y)
recursos = ['hora', 'dia_da_semana', 'dia_do_ano', 'mes', 'Temperatura']
alvo = 'Total_Demanda_KWh'

X = dados_brutos[recursos]
y = dados_brutos[alvo]

# Dividir os dados em conjuntos de treinamento e teste
# Usamos 80% para treinar o modelo e 20% para testar a sua precisão
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

print("Dados preparados para o treinamento do modelo.")

# Instanciar o modelo
modelo = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)

# Treinar o modelo com os dados de treinamento
modelo.fit(X_treino, y_treino)

print("Modelo treinado com sucesso!")

# Fazer previsões no conjunto de teste
previsoes = modelo.predict(X_teste)

# Calcular as métricas de desempenho
mse = mean_squared_error(y_teste, previsoes)
r2 = r2_score(y_teste, previsoes)

print(f"\n--- Avaliação do Modelo ---")
print(f"Erro Quadrático Médio (MSE): {mse:.2f}")
print(f"R-quadrado (R²): {r2:.2f}")

# Exibir um gráfico de comparação entre valores reais e previstos
plt.figure(figsize=(10, 6))
plt.scatter(y_teste, previsoes, alpha=0.5)
plt.plot([y_teste.min(), y_teste.max()], [y_teste.min(), y_teste.max()], '--r', linewidth=2)
plt.title('Valores Reais vs. Valores Previstos')
plt.xlabel('Valores Reais de Demanda (KWh)')
plt.ylabel('Valores Previstos de Demanda (KWh)')
plt.grid(True)
plt.show()