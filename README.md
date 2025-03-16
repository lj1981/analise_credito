# analise_credito Seu resultado e totalmente ficticio e nem um dos dados e real .


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

 
