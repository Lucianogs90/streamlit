import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("titanic.csv")

st.write("# Titanic.csv")

df_stats = df.groupby('Sex')['Age'].mean()

st.write("Média de idade por gênero")
st.dataframe(df_stats)

df_graf = px.histogram(df_stats, x=['male', 'female'], y='Age')

st.plotly_chart(df_graf)