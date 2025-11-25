import streamlit as st # Construir Dashboards
import pandas as pd # Ler arquivos
#import plotly.express as px # Construir Gráficos

st.header('NÚMEROS MENSAIS DA CAPELA SAGRADO CORAÇÃO DE JESUS') # Título do Dashboard

st.markdown('# Números Mensais')
st.caption("Despesas")

st.set_page_config(layout="wide") # Configura a página para o modo wide

df=pd.read_excel('PAGAMENTOS.xlsx') # Lê o arquivo Excel
df2=pd.read_excel('RECEBIMENTOS.xlsx') # Lê o arquivo Excel
df['DATA']=pd.to_datetime(df['DATA']) # Converte a coluna DATA para datetime

#st.bar_chart(df) # Gráfico de linha com os dados do DataFrame
#if st.sidebar.button('Exibir Gráfico'):
#    fig = px.bar(df, x='DATA', y='VALOR', title='Despesas Mensais') # Cria um gráfico de barras
#    st.plotly_chart(fig) # Exibe o gráfico no Streamlit

opcao=st.sidebar.selectbox(
    'Selecione uma opção:',
    ('Ver Recebimento', 'Ver Pagamentos','Ver Gráfico')
)

if opcao == 'Ver Recebimento':
    st.dataframe(df2) # Exibe o DataFrame como uma tabela interativa
elif opcao == 'Ver Pagamentos':
    #fig = px.line(df, x='DATA', y='VALOR', title='Despesas Mensais') # Cria um gráfico de linhas
    #st.plotly_chart(fig) # Exibe o gráfico no Streamlit
    st.dataframe(df) # Exibe o DataFrame como uma tabela interativa
elif opcao == 'Ver Gráfico':
    st.line_chart(df) # Cria um gráfico de barras
    st.line_chart(df2) # Cria um gráfico de barras
    #st.line_chart(fig) # Exibe o gráfico no Streamlit
    #st.line_chart(fig2) # Exibe o gráfico no Streamlit