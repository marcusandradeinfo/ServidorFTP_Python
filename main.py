import streamlit as st 
from Controller import controllerbuttons

def Main():
    st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)
    st.text("SERVIDOR FTP")
    st.divider()

    ### Criação das variáveis de Sessão para controle da Página
    if "txtip" not in st.session_state:
        st.session_state.txtip = False


    with st.container(height=100):
        teste, teste2, teste3 = st.columns([1, 0.5, 4], vertical_alignment='top')
        ##### st.sessionstate.txtip será habilitada ou não
        teste.text_input("Insira o IP do Servidor", disabled=st.session_state.txtip)
        dados_porta = teste2.text_input("Porta")
    btn_buscar_ip = st.button("Buscar IP")
    if btn_buscar_ip:
        result_ip = controllerbuttons.BuscarIP()
        if result_ip is not None and dados_porta != "":
            print(f"Dados da variável porta: {dados_porta}")
            st.success(f'Endereço de IP: {result_ip} obtido com exito !', icon="✅")
            st.session_state.txtip = True
            st.rerun()
        else:
             st.error("Favor inserir uma Porta para o Servidor", icon="🚨")
             st.session_state.txtip = False
             st.rerun()
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
