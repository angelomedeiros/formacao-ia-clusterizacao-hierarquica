import streamlit as st
import pandas as pd

# Carregar dados e colocar no cache do Streamlit
@st.cache_data
def carregar_dados():
    return pd.read_csv('datasets/clusterizacao_laptops.csv')

df = carregar_dados()

# Sidebar para filtro
st.sidebar.header('Filtro')

# Selecionar modelos
model = st.sidebar.selectbox('Selecionar Modelo', df['model'].unique())

# Filtrar dados
df_laptops_model = df[df['model'] == model]

# Filtrar cluster do modelo escolhido
df_laptops_final = df[df['cluster'] == df_laptops_model.iloc[0]['cluster']]

# Mostrar modelos
st.write("Recomendações de modelos")
st.table(df_laptops_final)
