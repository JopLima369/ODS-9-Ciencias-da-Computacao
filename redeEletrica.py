import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib # Usaremos essa biblioteca para salvar e carregar o modelo

# 1. Carregar os dados e preparar o modelo (o mesmo código da Etapa 3)
dados_brutos = pd.read_csv('smartgrid_dados_simulados.csv', index_col='Unnamed: 0', parse_dates=True)
dados_brutos.index.name = 'Data_Hora'
dados_brutos['hora'] = dados_brutos.index.hour
dados_brutos['dia_da_semana'] = dados_brutos.index.dayofweek
dados_brutos['dia_do_ano'] = dados_brutos.index.dayofyear
dados_brutos['mes'] = dados_brutos.index.month

recursos = ['hora', 'dia_da_semana', 'dia_do_ano', 'mes', 'Temperatura']
alvo = 'Total_Demanda_KWh'

X = dados_brutos[recursos]
y = dados_brutos[alvo]

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
modelo.fit(X_treino, y_treino)

# Salvar o modelo treinado para uso posterior
joblib.dump(modelo, 'modelo_demanda.pkl')
print("Modelo de previsão salvo como 'modelo_demanda.pkl'.")

# 2. Carregar o modelo e os dados de teste
modelo_carregado = joblib.load('modelo_demanda.pkl')
# Usaremos o conjunto de teste para simular o "mundo real"
X_teste['Demanda_Real_KWh'] = y_teste.values
X_teste['Solar_KWh'] = dados_brutos.loc[X_teste.index, 'Solar_KWh']
X_teste['Eolica_KWh'] = dados_brutos.loc[X_teste.index, 'Eolica_KWh']

# 3. Fazer as previsões de demanda
X_teste['Demanda_Prevista_KWh'] = modelo_carregado.predict(X_teste[recursos])

# Assegurar que as previsões não são negativas
X_teste['Demanda_Prevista_KWh'][X_teste['Demanda_Prevista_KWh'] < 0] = 0

# 4. Implementar o Algoritmo de Otimização
def otimizar_distribuicao(row):
    demanda_prevista = row['Demanda_Prevista_KWh']
    solar_disponivel = row['Solar_KWh']
    eolica_disponivel = row['Eolica_KWh']

    geracao_renovavel_total = solar_disponivel + eolica_disponivel
    
    # Energia renovável que pode ser usada para suprir a demanda
    energia_renovavel_usada = min(demanda_prevista, geracao_renovavel_total)
    
    # Energia que precisa ser gerada por fontes não renováveis
    energia_backup_necessaria = demanda_prevista - energia_renovavel_usada
    
    return pd.Series([energia_renovavel_usada, energia_backup_necessaria])

X_teste[['Renovavel_Usada', 'Backup_Necessario']] = X_teste.apply(otimizar_distribuicao, axis=1)

print("\nAlgoritmo de otimização executado com sucesso.")

# 5. Análise e Visualização dos Resultados
plt.figure(figsize=(12, 7))

# Pegar uma amostra de 2 dias para visualização
amostra = X_teste.head(48)

# Plotar a demanda real e a distribuição otimizada
plt.plot(amostra.index, amostra['Demanda_Real_KWh'], label='Demanda Real', color='black', linewidth=2, linestyle='--')
plt.bar(amostra.index, amostra['Renovavel_Usada'], label='Energia Renovável Usada', color='green', alpha=0.7)
plt.bar(amostra.index, amostra['Backup_Necessario'], bottom=amostra['Renovavel_Usada'], label='Energia de Backup Necessária', color='red', alpha=0.7)

plt.title('Demanda de Energia vs. Distribuição Otimizada (Amostra de 2 Dias)')
plt.xlabel('Data e Hora')
plt.ylabel('Energia (KWh)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--')
plt.show()

# Calcular a porcentagem de energia renovável usada
porcentagem_renovavel = (X_teste['Renovavel_Usada'].sum() / X_teste['Demanda_Real_KWh'].sum()) * 100
print(f"\n--- Resumo da Otimização ---")
print(f"Porcentagem da demanda total suprida por energia renovável: {porcentagem_renovavel:.2f}%")