import streamlit as st
from poo.view.View import View

class mensagensUI:

    __page = 'criptografados'
    __last_cript = None

    @classmethod
    def main(cls):
        if cls.__page == 'criptografados':
            dados, detalhe = st.columns((6,1))
            with dados:
                st.subheader("Mensagens")
            with detalhe:
                if st.button('Atualizar', key='voltar'):
                    st.rerun()

            with st.container(border=True):
                cript = View.listar_criptografados()
                if cript == None or len(cript) == 0:
                    st.write("Sem mensagens cadastradas")
                else:
                    for c in cript:
                        with st.container(border=True):
                            dados, detalhe = st.columns((5,1)) 
                            with dados:
                                st.write(f'**Mensagem Criptografada nº** {c.id}')
                            
                            with detalhe:
                                if st.button('Detalhes', key=f'detalhes{c.id}'):
                                    cls.__last_cript = c
                                    cls.__page = 'detalhes'
                                    st.rerun()

        elif cls.__page == 'detalhes':
            with st.container(border=True):
                cript = cls.__last_cript
                cliente = View.buscar_cliente_id(cript.id_cliente)
                decript = View.buscar_descriptografado_id(cript.id)
                
                st.write(f'**Mensagem Criptografada nº** {cript.id} | **Enviada por:**{cliente.ip}')
                st.write(f'**Mensagem Criptografada:** {cript.msg}')
                st.write(f'**Mensagem Descriptografada:**')
                st.write(f'**cpu:** {decript.cpu} | **mem:** {decript.mem} | **disk:** {decript.disk} | **temp:** {decript.temp}')

                if st.button('Voltar'):
                    cls.__page = 'criptografados'
                    cls.__last_cript = None
                    st.rerun()