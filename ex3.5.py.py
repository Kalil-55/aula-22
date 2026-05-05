#Crie uma lista de nomes simulando um banco de dados. Permita que o usuário: Escolha um nome para editar (com st.selectbox()); Digite o novo nome e clique em “Atualizar”; Ou clique em “Excluir” para removê-lo da lista. Dica: use condicionais com if e mensagens com st.success().
import sqlite3 as sq

import streamlit as st


st.title ("Exercício 04")

nome = st.text_input('digite o nome do usuário')

btn = st.button ('Aperte aqui')


escolha = st.selectbox("Escolha uma opção", ["atualizar", "excluir"])

if btn:
    st.write("Você clicou no primeiro botão")

if btn2:
    st.write("Confirmação realizada")

if btn:
    if escolha == atualizar:
        st.success(f'{nome} será atualizado')
    elif escolha == excluir:
        st.success(f'{nome} será excluído')

















 