import streamlit as st 
import time
from Controller import servidor


def Main():
    server = servidor.ServerFtp()
    st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)
    st.text("SERVIDOR FTP")
    st.divider()
    if "txtip" not in st.session_state:
         st.session_state.txtip = False
    if "log" not in st.session_state:
        st.session_state.log = ""
    if "numip" not in st.session_state:
        st.session_state.numip = None


    with st.container(height=100):
        teste,teste2,teste3 = st.columns([1,0.5,4],vertical_alignment='top')
        result_ip = teste.text_input("Insira o IP do Servidor",disabled=st.session_state.txtip)
        result_porta = teste2.text_input("Porta")
    btn_buscar_ip = st.button("Buscar IP")
    if btn_buscar_ip:
        result_ip = server.obter_ip()
        if result_ip is not None:
            st.session_state.txtip = True
            print(f"result ip: {result_ip}")
            st.session_state.numip = result_ip
            print(f"result ip: {st.session_state.numip}")
            st.success(f'Endereço de IP: {result_ip} obtido com exito !', icon="✅")
            time.sleep(2)
            # st.rerun()
            print(f"result ip: {st.session_state.numip}")

    coltxtusuario , coltxtsenha = st.columns([1,1])
    with coltxtusuario:
        txtuser = st.text_input("Usuário")
    with coltxtsenha:
        txtsenha = st.text_input("Senha")
    col_btn_iniciar, col_btn_pausar, col_espaco = st.columns([1,1,6])
    with col_btn_iniciar:
        btn_iniciar = st.button("Iniciar Servidor")
        if btn_iniciar:
            print(st.session_state.numip)
            if st.session_state.numip is not None and st.session_state.numip != "":
                if result_porta != "" and txtuser != "" and txtsenha != "":
                    print(f"Servidor FTP iniciado: Ip: {st.session_state.numip}, Porta: {result_porta}, Usuário: {txtuser}, Senha: {txtsenha} ")
                    result_conexao_server = server.start_server(st.session_state.numip,result_porta,txtuser,txtsenha)
                    st.session_state.log = "Servidor Iniciado"
                    time.sleep(1)
                    st.session_state.log = result_conexao_server
                else:
                    st.session_state.log = "Servidor não pode ser iniciado erro na porta, usuário ou senha"
            else:
                st.session_state.log ="Servidor não iniciado favor verificar número de IP"
    with col_btn_pausar:
        btn_pausar = st.button("Pausar Servidor")
        if btn_pausar:
            result_stop_server = server.stop_server()
            st.session_state.log = result_stop_server
    with col_espaco:
        pass
    st.divider()
    st.text_area("Log Servidor",value=st.session_state.log)
if __name__ == "__main__":
    Main()
