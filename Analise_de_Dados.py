#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
tabela = pd.read_csv("telecom_users.csv")

# Analisar a base e identificar o que precisa de tratamento

# excluir coluna Unnamed: 0
tabela = tabela.drop("Unnamed: 0", axis=1)

# transformar coluna Total Gasto em valor numerico
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# Excluir valores vazios
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)

# display(tabela)


# In[20]:


# Análise Inicial
print(tabela['Churn'].value_counts(normalize=True).map('{:.2%}'.format))

from pandas import DataFrame

tab = pd.DataFrame()
tab['Churn'] = tabela['Churn'].value_counts(normalize=True).map('{:.2%}'.format)
# display(tab) -- comando disponível apenas no jupyter


# In[14]:


# Análise detalhada (comparando demais coluna com o Churn)

import plotly.express as px

# Criar um gráfico de comparação com Churn PARA CADA COLUNA

for coluna in tabela:
    grafico = px.histogram(tabela,x=coluna,color='Churn',text_auto=True)
    grafico.show()




# In[ ]:


# Conclusões
# Clientes com famílias maiores(casados e com mais dependentes)tem menos cancelamento
# Clientes nos primeiros meses de serviço cancelam mais
# Clientes no plano mensal cancelam mais
# Clientes que pagam no boleto cancelam mais
# CLientes com menos servios contratados tem maior tendência a cancelar
# Clientes com fatura digital tem maior cancelamento

