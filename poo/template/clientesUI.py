import streamlit as st
from poo.view.View import View
import time

class clientesUI:
    @staticmethod
    def main():
        st.subheader("Clientes")
        
        with st.container(border=True):
            clientes = View.listar_clientes()
            if clientes == None or len(clientes) == 0:
                st.write("Sem clientes cadastrados")
            else:
                for cliente in clientes:
                    st.write(f"IP: {cliente.ip}")
            
            time.sleep(5)
            st.rerun()