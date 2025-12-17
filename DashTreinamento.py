import streamlit as st # Construir Dashboards
import pandas as pd # Ler arquivos
import datetime # Manipular datas
import plotly.express as px # Construir Gráficos

st.header('NÚMEROS MENSAIS DA CAPELA SAGRADO CORAÇÃO DE JESUS') # Título do Dashboard

st.markdown('# Números Mensais')
st.caption("Demonstrativos")

st.set_page_config(layout="wide") # Configura a página para o modo wide

df=pd.read_excel('PAGAMENTOS.xlsx') # Lê o arquivo Excel
df2=pd.read_excel('RECEBIMENTOS.xlsx') # Lê o arquivo Excel


df['DATA']=df['DATA'].dt.date # Extrai apenas a data (sem hora)
df2['DATA']=df2['DATA'].dt.date # Extrai apenas a data (

df=df.sort_values(by='DATA', ascending=False) # Ordena o DataFrame pela coluna DATA em ordem decrescente

df["Month"]=df["DATA"].apply(lambda x: str(x.year) + '-' + str(x.month)) # Extrai o mês e ano da coluna DATA
df2["Month"]=df2["DATA"].apply(lambda x: str(x.year) + '-' + str(x.month)) # Extrai o mês e ano da coluna DATA

month=st.sidebar.selectbox("Mês", df["Month"].unique()) # Cria um selectbox na barra lateral

df_filtered=df[df["Month"]==month] # Filtra o DataFrame pelo mês selecionado
#df2_filtered=df2[df2["Month"]==month] # Filtra o DataFrame pelo mês selecionado
df_filtered

col1, col2=st.columns(2) # Cria duas colunas
col3, col4, col5=st.columns(3) # Cria mais três colunas

fig_data=px.bar(df_filtered, x='DATA', y='VALOR', color='DESCRIÇÃO', title='Pagamentos') # Cria um gráfico de barras 
col1.plotly_chart(fig_data, use_container_width=True) # Exibe o gráfico na coluna 1

fig_cred=px.pie(df_filtered, names='CREDOR', values='VALOR',
                title='Pagamentos por Credor') # Cria um gráfico de pizza 
col2.plotly_chart(fig_cred) # Exibe o gráfico na coluna 2
