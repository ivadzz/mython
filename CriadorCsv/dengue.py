import pandas as pd
import numpy as np
import random

estados = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", "Espírito Santo", "Goiás",
    "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco",
    "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina",
    "São Paulo", "Sergipe", "Tocantins"
]

meses_anos = []
for ano in range(2014, 2020):
    for mes in range(1, 13):
        meses_anos.append(f"{mes:02d}-{ano}")

def introduzir_dados_faltantes(data, porcentagem=0.1):
    dados_faltantes = data.copy().astype(float)  
    num_dados_faltantes = int(porcentagem * data.size)
    indices_faltantes = np.random.choice(data.size, num_dados_faltantes, replace=False)
    dados_faltantes.ravel()[indices_faltantes] = np.nan
    return dados_faltantes

data = {
    "ID": [],
    "Estado": [],
    "Mês-Ano": [],
    "Casos": [],
    "Óbitos": [],
    "Hospitalizações": [],
    "Semana_Epidemiológica": []
}

for mes_ano in meses_anos:
    for estado in estados:
        data["ID"].append(len(data["ID"]) + 1)
        data["Estado"].append(estado)
        data["Mês-Ano"].append(mes_ano)
        casos = np.random.randint(0, 5000)
        obitos = np.random.randint(0, 100)
        hospitalizacoes = np.random.randint(0, 500)
        
        casos = introduzir_dados_faltantes(np.array([casos]))[0]
        obitos = introduzir_dados_faltantes(np.array([obitos]))[0]
        hospitalizacoes = introduzir_dados_faltantes(np.array([hospitalizacoes]))[0]
        
        data["Casos"].append(casos)
        data["Óbitos"].append(obitos)
        data["Hospitalizações"].append(hospitalizacoes)
        data["Semana_Epidemiológica"].append(random.randint(1, 53))

df = pd.DataFrame(data)

df[['Mês', 'Ano']] = df['Mês-Ano'].str.split('-', expand=True)

df = df[['ID', 'Estado', 'Mês-Ano', 'Mês', 'Ano', 'Casos', 'Óbitos', 'Hospitalizações', 'Semana_Epidemiológica']]

csv_path = "dengue.csv"
df.to_csv(csv_path, index=False)

print(f"Arquivo salvo em: {csv_path}")
