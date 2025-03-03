import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from poo.view.View import View
import time

class dadosUI:

    @staticmethod
    def main():
        st.subheader("Dados")

        for cliente in View.listar_clientes():
            with st.container(border=True):
                st.write(f"IP: {cliente.ip}")

                categorias = ['CPU', 'MEMORIA', 'DISCO', 'TEMPERATURA']
                dados = View.buscar_descriptografado_id_cliente(cliente.id)
                if dados != None:
                    cpu = mem = disk = temp = 0
                    for d in dados:
                        cpu = cpu + d.cpu
                        mem = mem + d.mem
                        disk = disk + d.disk
                        temp = temp + d.temp

                    cpu = cpu / len(dados)
                    mem = mem / len(dados)
                    disk = disk / len(dados)
                    temp = temp / len(dados)
                    
                    valores = [cpu, mem, disk, temp]

                    df = pd.DataFrame({'Categoria': categorias, 'Valor': valores})

                    fig, ax = plt.subplots()
                    ax.bar(df['Categoria'], df['Valor'], color='skyblue')
                    ax.set_xlabel('Categoria')
                    ax.set_ylabel('Valor')
                    ax.set_title('Gráfico de Barras')

                    st.pyplot(fig)

                else:
                    st.error("Sem dados cadastrados")

        time.sleep(5)
        st.rerun()

        # categorias = ['A', 'B', 'C', 'D', 'E']
        # valores = np.random.randint(1, 10, size=5)

        # df = pd.DataFrame({'Categoria': categorias, 'Valor': valores})

        # st.title('Exemplo de Gráfico de Barras com Streamlit')

        # fig, ax = plt.subplots()
        # ax.bar(df['Categoria'], df['Valor'], color='skyblue')
        # ax.set_xlabel('Categoria')
        # ax.set_ylabel('Valor')
        # ax.set_title('Gráfico de Barras')

        # st.pyplot(fig)