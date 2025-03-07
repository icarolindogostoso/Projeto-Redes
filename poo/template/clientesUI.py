import streamlit as st
from poo.view.View import View

class clientesUI:
    @staticmethod
    def main():
        dados, detalhe = st.columns((6,1))
        with dados:
            st.subheader("Clientes")
        with detalhe:
            if st.button('Atualizar', key='voltar'):
                st.rerun()
        
        with st.container(border=True):
            clientes = View.listar_clientes()
            if clientes == None or len(clientes) == 0:
                st.write("Sem clientes cadastrados")
            else:
                for cliente in clientes:
                    st.write(f"IP: {cliente.ip}")