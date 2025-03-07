import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from poo.view.View import View

class dadosUI:

    __page = 'dados'
    __last_data = None

    @classmethod
    def main(cls):
        st.empty()
        if cls.__page == 'dados':
            dados, detalhe = st.columns((6,1))
            with dados:
                st.subheader("Dados")
            with detalhe:
                if st.button('Atualizar', key='voltar'):
                    st.rerun()

            with st.container(border=True):
                categorias = ['CPU', 'MEMORIA', 'DISCO', 'TEMPERATURA']
                dados = View.listar_descriptografados()
                if len(dados) > 0:
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
                    ax.set_title('Média de Dados')

                    st.pyplot(fig)

                    dados, detalhe = st.columns((6,1))

                    with detalhe:
                        if st.button('Detalhes', key='detalhes'):
                            cls.__page = 'detalhes'
                            st.rerun()

                else:
                    st.warning("Sem dados cadastrados")

        elif cls.__page == 'detalhes':
            dados, detalhe, detalhe2 = st.columns((5,1,1))
            with dados:
                st.subheader("Dados")
            with detalhe:
                if st.button('Voltar', key='voltar'):
                    cls.__page = 'dados'
                    st.rerun()
            with detalhe2:
                if st.button('Atualizar', key='atualizar'):
                    st.rerun()

            for cliente in View.listar_clientes():
                with st.container(border=True):
                    st.write(f"IP: {cliente.ip}")

                    categorias = ['CPU', 'MEMORIA', 'DISCO', 'TEMPERATURA']
                    dados = View.buscar_descriptografado_id_cliente(cliente.id)
                    if len(dados) > 0:
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