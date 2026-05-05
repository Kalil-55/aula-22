#Crie um aplicativo simples com Streamlit que tenha: Um campo de texto para digitar o nome de um usuário; Um campo de texto para digitar a função dele (ex: “Professor”, “Aluno”); Um botão “Salvar” que mostre uma mensagem de sucesso quando clicado. Dica: use st.text_input() e st.button().


import streamlit as st

#st. session_state.lista =[]

#python -m streamlit run ikhno.py


st.title ("Exercício 01")

nome = st.text_input("Digite o nome do usuário")

btn = st.button('Butão')

if btn: 
    st. success("È ISSO AÍ!!")
    
