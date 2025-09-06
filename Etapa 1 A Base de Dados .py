<<<<<<< HEAD
import pandas as pd
import numpy as np

# 1. Definição do Período de Tempo
# Crie uma série de datas a cada hora por um ano
data_hora = pd.date_range(start='2024-01-01', end='2025-01-01', freq='H')

# 2. Simulação de Dados de Consumo
consumo = pd.DataFrame(index=data_hora)

# Fatores sazonais (mais consumo no verão/inverno, menos na primavera/outono)
fator_estacao = np.sin(2 * np.pi * (consumo.index.dayofyear / 365) - np.pi/2) + 1.5

# Consumo Base para cada zona
consumo_residencial_base = 100
consumo_industrial_base = 500
consumo_comercial_base = 200

# Geração de dados simulados com variações diárias e sazonais
consumo['Residencial_KWh'] = (consumo_residencial_base * (np.sin(2 * np.pi * consumo.index.hour / 24) + 1.5)) * fator_estacao + np.random.normal(0, 10, len(consumo))
consumo['Industrial_KWh'] = (consumo_industrial_base * (np.cos(2 * np.pi * consumo.index.hour / 24) + 1) * (consumo.index.weekday < 5).astype(int)) * fator_estacao + np.random.normal(0, 50, len(consumo))
consumo['Comercial_KWh'] = (consumo_comercial_base * (np.sin(2 * np.pi * (consumo.index.hour - 8) / 24) + 1.5) * (consumo.index.hour >= 8).astype(int) * (consumo.index.hour < 18).astype(int)) * fator_estacao + np.random.normal(0, 20, len(consumo))

# Somar para ter o consumo total
consumo['Total_Demanda_KWh'] = consumo['Residencial_KWh'] + consumo['Industrial_KWh'] + consumo['Comercial_KWh']

# Assegurar que não temos valores negativos
consumo[consumo < 0] = 0

# 3. Simulação de Fontes de Energia
geracao = pd.DataFrame(index=data_hora)

# Geração solar: mais energia durante o dia (pico ao meio-dia)
geracao['Solar_KWh'] = (1000 * np.sin(2 * np.pi * (geracao.index.hour - 6) / 12) * (geracao.index.hour >= 6).astype(int) * (geracao.index.hour <= 18).astype(int)) + np.random.normal(0, 50, len(geracao))

# Geração eólica: mais aleatória, mas com alguma variação diária
geracao['Eolica_KWh'] = 100 + 50 * np.sin(2 * np.pi * geracao.index.hour / 24) + np.random.normal(0, 100, len(geracao))

# Assegurar que não temos valores negativos
geracao[geracao < 0] = 0

# 4. Junção dos Dados
# Unir os DataFrames
dados_brutos = pd.concat([consumo, geracao], axis=1)

# Adicionar outros fatores que podem ser úteis para o modelo
dados_brutos['Temperatura'] = np.random.randint(10, 40, size=len(dados_brutos)) + np.sin(2 * np.pi * (dados_brutos.index.dayofyear - 80) / 365) * 15
dados_brutos['Dia_da_Semana'] = dados_brutos.index.dayofweek
dados_brutos['Fim_de_Semana'] = dados_brutos.index.dayofweek >= 5

# Salvar o DataFrame final em um arquivo CSV
dados_brutos.to_csv('smartgrid_dados_simulados.csv')

print("Dados simulados gerados com sucesso e salvos em 'smartgrid_dados_simulados.csv'.")
print("As primeiras 5 linhas do seu DataFrame:")
=======
import pandas as pd
import numpy as np

# 1. Definição do Período de Tempo
# Crie uma série de datas a cada hora por um ano
data_hora = pd.date_range(start='2024-01-01', end='2025-01-01', freq='H')

# 2. Simulação de Dados de Consumo
consumo = pd.DataFrame(index=data_hora)

# Fatores sazonais (mais consumo no verão/inverno, menos na primavera/outono)
fator_estacao = np.sin(2 * np.pi * (consumo.index.dayofyear / 365) - np.pi/2) + 1.5

# Consumo Base para cada zona
consumo_residencial_base = 100
consumo_industrial_base = 500
consumo_comercial_base = 200

# Geração de dados simulados com variações diárias e sazonais
consumo['Residencial_KWh'] = (consumo_residencial_base * (np.sin(2 * np.pi * consumo.index.hour / 24) + 1.5)) * fator_estacao + np.random.normal(0, 10, len(consumo))
consumo['Industrial_KWh'] = (consumo_industrial_base * (np.cos(2 * np.pi * consumo.index.hour / 24) + 1) * (consumo.index.weekday < 5).astype(int)) * fator_estacao + np.random.normal(0, 50, len(consumo))
consumo['Comercial_KWh'] = (consumo_comercial_base * (np.sin(2 * np.pi * (consumo.index.hour - 8) / 24) + 1.5) * (consumo.index.hour >= 8).astype(int) * (consumo.index.hour < 18).astype(int)) * fator_estacao + np.random.normal(0, 20, len(consumo))

# Somar para ter o consumo total
consumo['Total_Demanda_KWh'] = consumo['Residencial_KWh'] + consumo['Industrial_KWh'] + consumo['Comercial_KWh']

# Assegurar que não temos valores negativos
consumo[consumo < 0] = 0

# 3. Simulação de Fontes de Energia
geracao = pd.DataFrame(index=data_hora)

# Geração solar: mais energia durante o dia (pico ao meio-dia)
geracao['Solar_KWh'] = (1000 * np.sin(2 * np.pi * (geracao.index.hour - 6) / 12) * (geracao.index.hour >= 6).astype(int) * (geracao.index.hour <= 18).astype(int)) + np.random.normal(0, 50, len(geracao))

# Geração eólica: mais aleatória, mas com alguma variação diária
geracao['Eolica_KWh'] = 100 + 50 * np.sin(2 * np.pi * geracao.index.hour / 24) + np.random.normal(0, 100, len(geracao))

# Assegurar que não temos valores negativos
geracao[geracao < 0] = 0

# 4. Junção dos Dados
# Unir os DataFrames
dados_brutos = pd.concat([consumo, geracao], axis=1)

# Adicionar outros fatores que podem ser úteis para o modelo
dados_brutos['Temperatura'] = np.random.randint(10, 40, size=len(dados_brutos)) + np.sin(2 * np.pi * (dados_brutos.index.dayofyear - 80) / 365) * 15
dados_brutos['Dia_da_Semana'] = dados_brutos.index.dayofweek
dados_brutos['Fim_de_Semana'] = dados_brutos.index.dayofweek >= 5

# Salvar o DataFrame final em um arquivo CSV
dados_brutos.to_csv('smartgrid_dados_simulados.csv')

print("Dados simulados gerados com sucesso e salvos em 'smartgrid_dados_simulados.csv'.")
print("As primeiras 5 linhas do seu DataFrame:")
>>>>>>> 32c774956a4447fbd830af6f03a7b5e11fb843d6
print(dados_brutos.head())