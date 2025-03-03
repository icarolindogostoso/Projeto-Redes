import streamlit as st
from poo.sistema.Servidor import Servidor
from multiprocessing import Process
from poo.template.clientesUI import clientesUI
from poo.template.mensagensUI import mensagensUI
from poo.template.dadosUI import dadosUI

class indexUI:
    @staticmethod
    def ligar_servidor():
        servidor = Servidor("0.0.0.0", 8000)
        servidor.ligar()

    @staticmethod
    def desligar_servidor():
        if 'server_process' in st.session_state:
            st.session_state.server_process.terminate()
            st.session_state.server_process.join()
            del st.session_state.server_process
            st.success("Servidor desligado com sucesso!")
        else:
            st.warning("O servidor já está desligado.")

    @staticmethod
    def menu():
        st.title("Servidor")

        # Opções do menu
        op = st.sidebar.radio('', ["Dados", "Clientes", "Mensagens"])
        
        match op.lower():
            case "dados":
                servidor_ligado = 'server_process' in st.session_state

                if servidor_ligado:
                    if st.button("Desligar Servidor"):
                        indexUI.desligar_servidor()
                        st.rerun()
                else:
                    if st.button("Ligar Servidor"):
                        st.session_state.server_process = Process(target=indexUI.ligar_servidor)
                        st.session_state.server_process.start()
                        st.success("Servidor ligado com sucesso!")
                        st.rerun()

                dadosUI.main()

            case "clientes":
                clientesUI.main()

            case "mensagens":
                mensagensUI.main()

    @staticmethod
    def main():
        indexUI.menu()

if __name__ == "__main__":
    indexUI.main()