import pandas as pd
import random
from datetime import datetime, timedelta
import requests

# Configurações gerais do dataset
n_linhas = 45000  # Definindo o número de linhas
ids = [random.randint(10 ** 10, 10 ** 11 - 1) for _ in range(n_linhas)]  # IDs com 11 dígitos

# Função para obter cidades, estados e bairros fictícios
estados = ["SP", "RJ", "MG", "RS", "BA", "PR", "SC", "PE", "CE", "GO"]
cidades = {"SP": ["São Paulo", "Campinas", "Santos"],
           "RJ": ["Rio de Janeiro", "Niterói", "Petrópolis"],
           "MG": ["Belo Horizonte", "Uberlândia", "Juiz de Fora"],
           "RS": ["Porto Alegre", "Caxias do Sul", "Pelotas"],
           "BA": ["Salvador", "Feira de Santana", "Ilhéus"],
           "PR": ["Curitiba", "Londrina", "Maringá"],
           "SC": ["Florianópolis", "Joinville", "Blumenau"],
           "PE": ["Recife", "Olinda", "Caruaru"],
           "CE": ["Fortaleza", "Caucaia", "Juazeiro do Norte"],
           "GO": ["Goiânia", "Anápolis", "Aparecida de Goiânia"]}
bairros = ["Centro", "Zona Sul", "Zona Norte", "Bairro Novo", "Vila Rica"]

# Listas de nomes fictícios
nomes = ["João Silva", "Maria Souza", "Carlos Oliveira", "Ana Lima", "Fernando Santos", "Juliana Costa"]

# Dados aleatórios
dados = []
for _ in range(n_linhas):
    id_cliente = ids.pop()
    nome_completo = random.choice(nomes)
    primeiro_nome, ultimo_nome = nome_completo.split()
    idade = random.randint(18, 60)
    genero = random.choice(["Masculino", "Feminino"])
    estado = random.choice(estados)
    cidade = random.choice(cidades[estado])
    bairro = random.choice(bairros)
    salario = round(random.uniform(1518, 10000), 2)
    patrimonio = round(random.uniform(salario * 2, salario * 10), 2)

    # Simulação dos últimos 3 meses
    emprestimos = [random.choice([0, round(random.uniform(500, salario * 1.5), 2)]) for _ in range(3)]
    financiamentos = [random.choice([0, round(random.uniform(500, salario * 2), 2)]) for _ in range(3)]
    parcelas = [e + f for e, f in zip(emprestimos, financiamentos)]

    # Cálculo do score baseado nos valores de empréstimos e financiamentos
    total_credito_utilizado = sum(parcelas) / 3
    percentual_uso = (total_credito_utilizado / salario) * 100 if salario > 0 else 100

    if percentual_uso == 0:
        score = 1000
    elif percentual_uso <= 10:
        score = random.randint(700, 900)
    elif percentual_uso <= 15:
        score = random.randint(599, 699)
    elif percentual_uso <= 30:
        score = random.randint(499, 598)
    else:
        score = random.randint(200, 498)

    # Definir status baseado no score
    if score >= 800:
        status = "Excelente"
    elif score >= 599:
        status = "Moderado"
    elif score >= 499:
        status = "Bom"
    else:
        status = "Ruim"

    # Crédito pré-aprovado
    credito_pre_aprovado = salario - total_credito_utilizado if status == "Excelente" or status == "Bom" else 0

    dados.append({
        "ID": id_cliente,
        "Nome": primeiro_nome + " " + ultimo_nome,
        "Idade": idade,
        "Gênero": genero,
        "Estado": estado,
        "Cidade": cidade,
        "Bairro": bairro,
        "Salário": f"R${salario:,.2f}",
        "Patrimônio": f"R${patrimonio:,.2f}",
        "Empréstimo_Mês1": f"R${emprestimos[0]:,.2f}",
        "Empréstimo_Mês2": f"R${emprestimos[1]:,.2f}",
        "Empréstimo_Mês3": f"R${emprestimos[2]:,.2f}",
        "Financiamento_Mês1": f"R${financiamentos[0]:,.2f}",
        "Financiamento_Mês2": f"R${financiamentos[1]:,.2f}",
        "Financiamento_Mês3": f"R${financiamentos[2]:,.2f}",
        "Parcelas_Médias": f"R${total_credito_utilizado:,.2f}",
        "Score": score,
        "Status": status,
        "Crédito_Pre_Aprovado": f"R${credito_pre_aprovado:,.2f}"
    })

# Criar DataFrame
df_credito = pd.DataFrame(dados)

# Centralizar títulos das colunas
df_credito.columns = [col.center(20) for col in df_credito.columns]

# Salvar em CSV
file_path = "dataset_credito_simulado.csv"
df_credito.to_csv(file_path, index=False, encoding="utf-8")
print(f"Arquivo CSV salvo em: {file_path}")
