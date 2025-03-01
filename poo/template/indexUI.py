import streamlit as st
from poo.sistema.Servidor import Servidor
from multiprocessing import Process
from poo.template.clientesUI import clientesUI
from poo.template.mensagensUI import mensagensUI

class indexUI:
    @staticmethod
    def ligar_servidor():
        servidor = Servidor("0.0.0.0", 8000)
        servidor.ligar()

    @staticmethod
    def menu():
        st.title("Servidor")

        op = st.sidebar.radio('',["Dados", "Clientes", "Mensagens"])
        
        match op.lower():
            case "dados":
                st.write("Dados")
            case "clientes":
                clientesUI.main()
            case "mensagens":
                mensagensUI.main()

    @staticmethod
    def main():
        
        if 'server_process' not in st.session_state:
            st.session_state.server_process = Process(target=indexUI.ligar_servidor)
            st.session_state.server_process.start()

        indexUI.menu()

if __name__ == "__main__":
    indexUI.main()