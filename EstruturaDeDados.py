<<<<<<< HEAD
import pandas as pd
import numpy as np

# 1. Defina a classe para gerenciar os dados
class RealTimeDataManager:
    def __init__(self):
        # A estrutura de dados principal é um dicionário (hash map)
        self.data_store = {}
    
    def load_data_from_csv(self, filename='smartgrid_dados_simulados.csv'):
        """Carrega os dados do CSV para o dicionário."""
        try:
            # Carrega o DataFrame do arquivo CSV
            df = pd.read_csv(filename, index_col='Unnamed: 0', parse_dates=True)
            
            # Converte cada linha do DataFrame em um dicionário e armazena no data_store
            for index, row in df.iterrows():
                # A chave do dicionário é o timestamp (data e hora)
                # O valor é um dicionário com todos os dados daquela linha
                self.data_store[index] = row.to_dict()
            print(f"Dados carregados com sucesso. Total de {len(self.data_store)} pontos de dados.")
        except FileNotFoundError:
            print(f"Erro: O arquivo '{filename}' não foi encontrado.")

    def get_data_by_timestamp(self, timestamp):
        """Busca os dados de um timestamp específico."""
        if timestamp in self.data_store:
            # A busca no dicionário é O(1) - instantânea
            return self.data_store[timestamp]
        else:
            print(f"Dados não encontrados para o timestamp: {timestamp}")
            return None

    def add_new_data_point(self, timestamp, data):
        """Simula a adição de um novo ponto de dado em tempo real."""
        self.data_store[timestamp] = data
        print(f"Novo ponto de dado adicionado para o timestamp: {timestamp}")

# --- Demonstração de uso ---
if __name__ == "__main__":
    # Crie uma instância da sua nova estrutura de dados
    manager = RealTimeDataManager()

    # Carregue os dados do CSV
    manager.load_data_from_csv()

    # Exemplo de como acessar dados de forma eficiente
    # Busque um dado para uma data e hora específica
    data_buscada = pd.to_datetime('2024-03-10 14:00:00')
    dados = manager.get_data_by_timestamp(data_buscada)
    
    if dados:
        print("\nDados encontrados para o timestamp buscado:")
        for key, value in dados.items():
            print(f"- {key}: {value:.2f}")

    # Exemplo de como simular a chegada de novos dados
    novo_timestamp = pd.to_datetime('2025-01-01 01:00:00')
    novo_dado = {
        'Residencial_KWh': 150.0,
        'Industrial_KWh': 50.0,
        'Comercial_KWh': 25.0,
        'Total_Demanda_KWh': 225.0,
        'Solar_KWh': 0.0,
        'Eolica_KWh': 120.0,
        'Temperatura': 20.0,
        'Dia_da_Semana': 6,
        'Fim_de_Semana': True
    }
    manager.add_new_data_point(novo_timestamp, novo_dado)
    
    # Acesso instantâneo ao novo dado
    print("\nVerificando o dado recém-adicionado:")
    print(manager.get_data_by_timestamp(novo_timestamp))
=======
import pandas as pd
import numpy as np

# 1. Defina a classe para gerenciar os dados
class RealTimeDataManager:
    def __init__(self):
        # A estrutura de dados principal é um dicionário (hash map)
        self.data_store = {}
    
    def load_data_from_csv(self, filename='smartgrid_dados_simulados.csv'):
        """Carrega os dados do CSV para o dicionário."""
        try:
            # Carrega o DataFrame do arquivo CSV
            df = pd.read_csv(filename, index_col='Unnamed: 0', parse_dates=True)
            
            # Converte cada linha do DataFrame em um dicionário e armazena no data_store
            for index, row in df.iterrows():
                # A chave do dicionário é o timestamp (data e hora)
                # O valor é um dicionário com todos os dados daquela linha
                self.data_store[index] = row.to_dict()
            print(f"Dados carregados com sucesso. Total de {len(self.data_store)} pontos de dados.")
        except FileNotFoundError:
            print(f"Erro: O arquivo '{filename}' não foi encontrado.")

    def get_data_by_timestamp(self, timestamp):
        """Busca os dados de um timestamp específico."""
        if timestamp in self.data_store:
            # A busca no dicionário é O(1) - instantânea
            return self.data_store[timestamp]
        else:
            print(f"Dados não encontrados para o timestamp: {timestamp}")
            return None

    def add_new_data_point(self, timestamp, data):
        """Simula a adição de um novo ponto de dado em tempo real."""
        self.data_store[timestamp] = data
        print(f"Novo ponto de dado adicionado para o timestamp: {timestamp}")

# --- Demonstração de uso ---
if __name__ == "__main__":
    # Crie uma instância da sua nova estrutura de dados
    manager = RealTimeDataManager()

    # Carregue os dados do CSV
    manager.load_data_from_csv()

    # Exemplo de como acessar dados de forma eficiente
    # Busque um dado para uma data e hora específica
    data_buscada = pd.to_datetime('2024-03-10 14:00:00')
    dados = manager.get_data_by_timestamp(data_buscada)
    
    if dados:
        print("\nDados encontrados para o timestamp buscado:")
        for key, value in dados.items():
            print(f"- {key}: {value:.2f}")

    # Exemplo de como simular a chegada de novos dados
    novo_timestamp = pd.to_datetime('2025-01-01 01:00:00')
    novo_dado = {
        'Residencial_KWh': 150.0,
        'Industrial_KWh': 50.0,
        'Comercial_KWh': 25.0,
        'Total_Demanda_KWh': 225.0,
        'Solar_KWh': 0.0,
        'Eolica_KWh': 120.0,
        'Temperatura': 20.0,
        'Dia_da_Semana': 6,
        'Fim_de_Semana': True
    }
    manager.add_new_data_point(novo_timestamp, novo_dado)
    
    # Acesso instantâneo ao novo dado
    print("\nVerificando o dado recém-adicionado:")
    print(manager.get_data_by_timestamp(novo_timestamp))
>>>>>>> 32c774956a4447fbd830af6f03a7b5e11fb843d6
    print(manager.get_data_by_timestamp(pd.to_datetime("2024-12-30 12:00:00")))