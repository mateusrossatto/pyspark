import pandas as pd
import streamlit as st

df_primeira_visualizacao = pd.read_csv('data/primeira_visualizacao.csv')
df_segunda_visualizacao = pd.read_csv('data/segunda_visualizacao.csv')
df_terceira_visualizacao = pd.read_csv('data/terceira_visualizacao.csv')
df_sintese_visualizacao = pd.read_csv('data/sintese_visualizacao.csv')

st.write('Projeto Final de Spark - Campanha Nacional de Vacinação contra Covid-19')
st.table(df_primeira_visualizacao)
st.table(df_segunda_visualizacao)
st.table(df_terceira_visualizacao)
st.table(df_sintese_visualizacao)
