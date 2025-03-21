import pandas as pd
import random
import requests


# Função para obter nomes populares do IBGE
def obter_nomes_ibge():
    url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        nomes = [item["nome"] for item in dados]
        return nomes
    return ["Carlos", "Ana", "Fernanda", "João", "Mariana"]  # Fallback caso a API falhe


# Função para obter estados e cidades do IBGE
def obter_localidades_ibge():
    estados_url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    municipios_url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"

    estados = {}
    resposta_estados = requests.get(estados_url)
    if resposta_estados.status_code == 200:
        for estado in resposta_estados.json():
            estados[estado["sigla"]] = []

    resposta_municipios = requests.get(municipios_url)
    if resposta_municipios.status_code == 200:
        for municipio in resposta_municipios.json():
            uf = municipio["microrregiao"]["mesorregiao"]["UF"]["sigla"]
            if uf in estados:
                estados[uf].append(municipio["nome"])

    return estados


# Lista de sobrenomes fictícios
sobrenomes = ["Silva", "Souza", "Oliveira", "Lima", "Santos", "Costa", "Almeida", "Mendes", "Gomes", "Xavier"]

# Lista de bairros genéricos
bairros = ["Centro", "Vila Nova", "Jardim América", "Parque Industrial", "Bela Vista", "Boa Esperança"]

# Obter dados da API IBGE
nomes_ibge = obter_nomes_ibge()
localidades = obter_localidades_ibge()

# Configurações do dataset
n_linhas = 10000  # Número de clientes
ids = [random.randint(10 ** 10, 10 ** 11 - 1) for _ in range(n_linhas)]

# Gerando os dados
dados = []
for _ in range(n_linhas):
    id_cliente = ids.pop()
    primeiro_nome = random.choice(nomes_ibge).capitalize()
    ultimo_nome = random.choice(sobrenomes)

    estado = random.choice(list(localidades.keys()))
    cidade = random.choice(localidades[estado])
    bairro = random.choice(bairros)

    idade = random.randint(18, 60)
    genero = random.choice(["Masculino", "Feminino"])
    salario = round(random.uniform(1518, 20000), 2)
    patrimonio = round(random.uniform(salario * 1.5, salario * 12), 2)

    # Probabilidade de pegar crédito
    prob_pegou_credito = random.random()
    if prob_pegou_credito < 0.3:
        emprestimos = [0, 0, 0]
        financiamentos = [0, 0, 0]
    else:
        emprestimos = [random.choice([0, round(random.uniform(500, salario * 1.5), 2)]) for _ in range(3)]
        financiamentos = [random.choice([0, round(random.uniform(500, salario * 2), 2)]) for _ in range(3)]

    parcelas = [e + f for e, f in zip(emprestimos, financiamentos)]
    total_credito_utilizado = sum(parcelas) / 3
    percentual_uso = (total_credito_utilizado / salario) * 100 if salario > 0 else 100

    if percentual_uso == 0:
        score = random.randint(850, 1000)
    elif percentual_uso <= 10:
        score = random.randint(700, 900)
    elif percentual_uso <= 25:
        score = random.randint(599, 699)
    elif percentual_uso <= 40:
        score = random.randint(499, 598)
    else:
        score = random.randint(200, 498)

    if score >= 800:
        status = "Excelente"
    elif score >= 600:
        status = "Bom"
    elif score >= 500:
        status = "Moderado"
    else:
        status = "Ruim"

    credito_pre_aprovado = round(random.uniform(0, salario * 1.5), 2) if status in ["Excelente", "Bom"] else 0

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

# Salvar em CSV
file_path = "dataset_credito_simulado.csv"
df_credito.to_csv(file_path, index=False, encoding="utf-8")
print(f"Arquivo CSV salvo em: {file_path}")
