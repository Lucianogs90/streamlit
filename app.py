import streamlit as st

st.title("App de exemplo")
st.write("Texto de exemplo")

with st.sidebar:
    st.write("Texto da sidebar")
    st.radio(
        label = 'Radio btn',
        options =['Teste1', 'Teste2']
        )
    st.checkbox(
        label='Testando checkbox'
    )
    st.date_input(
        label="Data"
    )
    st.slider(
        label="Slider",
        min_value=0,
        max_value=10
    )