import streamlit as st 


def Main():
    st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)
    st.text("SERVIDOR FTP")
    st.divider()
    with st.container(height=100):
        teste,teste2,teste3 = st.columns([1,0.5,4],vertical_alignment='top')
        teste.text_input("Insira o IP do Servidor")
        teste2.text_input("Porta")
    st.button("Buscar IP")
    txtusuario , txtsenha = st.columns([1,1])
    with txtusuario:
        st.text_input("Usuário")
    with txtsenha:
        st.text_input("Senha")
    btn_iniciar, btn_pausar, col_espaco = st.columns([1,1,6])
    with btn_iniciar:
        st.button("Iniciar Servidor")
    with btn_pausar:
        st.button("Pausar Servidor")
    with col_espaco:
        pass
    st.divider()
    st.text_area("Log Servidor")
if __name__ == "__main__":
    Main()
