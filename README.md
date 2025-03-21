**Documento Técnico: Geração de Dataset de Crédito**

### Introdução
Este documento técnico descreve o funcionamento do código desenvolvido para gerar um dataset simulado de informações financeiras de clientes. O objetivo é permitir a análise de crédito com dados realistas e variáveis a cada execução.

### Objetivo
Criar um dataset contendo informações detalhadas sobre clientes, incluindo nome, localização, salário, patrimônio, histórico de empréstimos e financiamentos, parcelas e score de crédito. O código garante que todas as informações financeiras sejam formatadas corretamente e que clientes com status "Ruim" ou "Moderado" não tenham crédito pré-aprovado.

### Estrutura do Dataset
O dataset gerado contém as seguintes colunas:

- **ID**: Identificador único do cliente (11 dígitos)
- **Nome Completo**: Primeiro e último nome do cliente
- **Estado**: Estado de residência
- **Cidade**: Cidade de residência
- **Bairro**: Bairro de residência
- **Salário**: Renda mensal do cliente (formatado como moeda)
- **Patrimônio**: Valor total do patrimônio do cliente (formatado como moeda)
- **Empréstimos Mês 1, 2 e 3**: Valor do empréstimo tomado em cada um dos últimos três meses (formatado como moeda)
- **Financiamentos Mês 1, 2 e 3**: Valor financiado pelo cliente nos últimos três meses (formatado como moeda)
- **Parcelas Médias**: Média do valor das parcelas mensais (formatado como moeda)
- **Score de Crédito**: Pontuação calculada com base no uso do crédito em relação ao salário
- **Status de Crédito**: Classificação do cliente com base no score:
  - **Excelente** (1000-800)
  - **Moderado** (799-599)
  - **Bom** (598-499)
  - **Ruim** (498-200)
- **Crédito Pré-Aprovado**: Valor do salário menos os empréstimos e financiamentos, limitado a R$ 0 para clientes com status "Ruim" ou "Moderado".

### Regras de Geração de Dados
1. Os dados são gerados aleatoriamente a cada execução para simular diferentes cenários reais.
2. Clientes podem ou não ter tomado empréstimos ou financiamentos nos últimos três meses.
3. O score é calculado proporcionalmente ao uso do crédito em relação ao salário do cliente.
4. O formato de moeda (“R$”) é aplicado a todas as colunas financeiras.
5. Os títulos das colunas estão centralizados para melhor leitura.
6. Clientes com status "Ruim" ou "Moderado" não têm crédito pré-aprovado.

### Como Utilizar o Código
1. Instale as dependências necessárias:
   ```bash
   pip install pandas random datetime requests
   ```
2. Execute o script Python.
3. O arquivo CSV será gerado no caminho especificado no código.
4. Utilize o dataset para análise de crédito conforme necessário.

### Dica de melhorias Futuras
- Adicionar comportamento de inadimplência baseado no histórico do cliente.
- Criar perfis de clientes com diferentes perfis de risco.
- Implementar integração com bases externas de dados para melhorar a precisão da simulação.

### Conclusão
Este código permite a geração de um dataset robusto e flexível para análise financeira e previsão de crédito, tornando-se uma ferramenta útil para estudos e desenvolvimento de modelos de machine learning.



- - v. 2 - - 


**Documento Técnico: Geração de Dataset de Crédito Simulado**

# Introdução
Este documento tem como objetivo descrever a utilização do código para gerar um dataset de crédito simulado, utilizando a API do IBGE para obter nomes, estados e cidades reais. O script gera um arquivo CSV contendo informações financeiras e de crédito de clientes fictícios.

# Requisitos
Antes de executar o código, certifique-se de ter os seguintes requisitos instalados:

- **Python 3.x**
- **Bibliotecas Necessárias:**
  ```sh
  pip install pandas requests
  ```

# Funcionamento do Código
O script segue os seguintes passos:

1. **Obter nomes reais do IBGE**
   - A API do IBGE fornece uma lista de nomes populares no Brasil.
   - Um nome é escolhido aleatoriamente e combinado com um sobrenome fictício.

2. **Obter estados e cidades reais do IBGE**
   - A API do IBGE fornece a lista de estados e cidades.
   - Cada cliente recebe um estado e uma cidade aleatória dentro desse estado.

3. **Gerar informações financeiras**
   - Idade entre 18 e 60 anos.
   - Salário entre R$ 1.518,00 e R$ 20.000,00.
   - Patrimônio baseado no salário.
   - Empréstimos e financiamentos gerados aleatoriamente.

4. **Calcular score de crédito**
   - Baseado na utilização do crédito em relação ao salário.
   - Classifica o status do cliente como **Excelente, Bom, Moderado ou Ruim**.

5. **Salvar os dados em CSV**
   - O dataset é salvo em um arquivo chamado `dataset_credito_simulado.csv`.

# Como Executar
1. Baixe o código Python.
2. Execute o script com o comando:
   ```sh
   python script.py
   ```
3. O arquivo CSV será gerado no diretório de execução do script.

# Formato do Dataset
O arquivo CSV gerado contém as seguintes colunas:

| ID | Nome | Idade | Gênero | Estado | Cidade | Bairro | Salário | Patrimônio | Empréstimos | Financiamentos | Score | Status | Crédito Pré-Aprovado |
|----|------|-------|---------|--------|--------|--------|---------|-----------|-------------|--------------|-------|--------|-----------------|

# Possíveis Problemas e Soluções
- **Erro de conexão com a API do IBGE**: Verifique sua conexão com a internet e tente novamente.
- **Arquivo CSV corrompido ou vazio**: Certifique-se de que o script foi executado corretamente e que os dados foram coletados.
- **Valores financeiros desbalanceados**: Os valores são gerados aleatoriamente, execute o script novamente para obter diferentes resultados.

# Conclusão
Este script permite gerar um dataset realista para análise de crédito, facilitando simulações e estudos financeiros. Qualquer dúvida ou sugestão pode ser encaminhada ao desenvolvedor responsável.





# Seu resultado e totalmente ficticio e nem um dos dados e real .



 
