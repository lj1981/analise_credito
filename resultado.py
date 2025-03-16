import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

# Carregar o dataset
caminho_arquivo = "/home/luiz/Downloads/Projetos_One/analise_credito/dataset_credito_simulado.csv"
df = pd.read_csv(caminho_arquivo)

# Limpar os nomes das colunas, removendo espaços extras
df.columns = df.columns.str.strip()

# Garantir que os nomes das colunas estão corretos
print("Nomes das colunas:", df.columns)

# Função para converter valores monetários
def converter_moeda(valor):
    # Verificar se o valor é numérico
    try:
        valor_float = float(valor)
        return f"R$ {valor_float:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return valor  # Se não for numérico, retorna o valor original

# Aplicar formatação às colunas financeiras
colunas_monetarias = ['Salário', 'Patrimônio', 'Empréstimo_Mês1', 'Empréstimo_Mês2', 'Empréstimo_Mês3',
                      'Financiamento_Mês1', 'Financiamento_Mês2', 'Financiamento_Mês3', 'Parcelas_Médias',
                      'Crédito_Pre_Aprovado']
for coluna in colunas_monetarias:
    # Verificar se a coluna existe no DataFrame antes de aplicar a formatação
    if coluna in df.columns:
        df[coluna] = df[coluna].apply(lambda x: converter_moeda(x) if pd.notnull(x) else x)
    else:
        print(f"A coluna '{coluna}' não foi encontrada no DataFrame.")

# Garantir que clientes com "Ruim" ou "Moderado" tenham crédito pré-aprovado igual a R$ 0
df.loc[df['Status'].isin(["Ruim", "Moderado"]), 'Crédito_Pre_Aprovado'] = "R$ 0,00"

# Criar gráficos
fig_score = px.histogram(df, x="Score", nbins=20, title="Distribuição do Score de Crédito",
                         labels={"Score": "Score de Crédito"}, color_discrete_sequence=["#636EFA"])

fig_status = px.pie(df, names='Status', title='Distribuição do Status de Crédito',
                     color_discrete_sequence=px.colors.qualitative.Set2)

fig_salario_credito = px.scatter(df, x='Salário', y='Crédito_Pre_Aprovado',
                                 title='Relação entre Salário e Crédito Pré-Aprovado',
                                 labels={'Salário': 'Salário (R$)', 'Crédito_Pre_Aprovado': 'Crédito Pré-Aprovado (R$)'},
                                 color_discrete_sequence=["#EF553B"])

# Criar o aplicativo Dash
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Dashboard de Análise de Crédito", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig_score),
    dcc.Graph(figure=fig_status),
    dcc.Graph(figure=fig_salario_credito)
])

# Executar o servidor Dash
if __name__ == '__main__':
    app.run_server(debug=True)
