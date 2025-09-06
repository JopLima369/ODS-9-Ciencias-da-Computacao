import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # Opcional, mas muito bom para gráficos

# Carregar o arquivo CSV
dados_brutos = pd.read_csv('smartgrid_dados_simulados.csv', index_col='Unnamed: 0', parse_dates=True)
dados_brutos.index.name = 'Data_Hora'

# Exibir as primeiras linhas para confirmar o carregamento
print("Dados carregados com sucesso. As primeiras 5 linhas:")
print(dados_brutos.head())

# Calcular a média de consumo por hora do dia
consumo_medio_diario = dados_brutos.groupby(dados_brutos.index.hour)['Total_Demanda_KWh'].mean()

plt.figure(figsize=(10, 6))
consumo_medio_diario.plot(kind='bar', color='skyblue')
plt.title('Consumo Médio de Energia por Hora do Dia')
plt.xlabel('Hora do Dia')
plt.ylabel('Consumo Médio (KWh)')
plt.grid(axis='y', linestyle='--')
plt.show()

# Pegar uma amostra de 7 dias para visualização mais clara
amostra_semanal = dados_brutos['2024-01-01':'2024-01-08']

plt.figure(figsize=(12, 7))
plt.plot(amostra_semanal.index, amostra_semanal['Residencial_KWh'], label='Residencial', color='blue')
plt.plot(amostra_semanal.index, amostra_semanal['Industrial_KWh'], label='Industrial', color='red')
plt.plot(amostra_semanal.index, amostra_semanal['Comercial_KWh'], label='Comercial', color='green')
plt.title('Consumo de Energia por Zona (Amostra de 1 Semana)')
plt.xlabel('Data e Hora')
plt.ylabel('Consumo (KWh)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 7))

# Pegar uma amostra menor para clareza
amostra_diaria = dados_brutos['2024-06-15':'2024-06-16']

plt.plot(amostra_diaria.index, amostra_diaria['Total_Demanda_KWh'], label='Demanda Total', color='black', linewidth=2)
plt.plot(amostra_diaria.index, amostra_diaria['Solar_KWh'], label='Geração Solar', color='orange')
plt.plot(amostra_diaria.index, amostra_diaria['Eolica_KWh'], label='Geração Eólica', color='purple')

plt.title('Demanda Total vs. Geração Renovável (Amostra de 1 Dia)')
plt.xlabel('Hora do Dia')
plt.ylabel('Energia (KWh)')
plt.legend()
plt.grid(True)
plt.show()