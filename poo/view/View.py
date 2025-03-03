from poo.model.cliente import Cliente
from poo.model.criptografado import Criptografado
from poo.model.descriptografado import Descriptografado
from poo.model.CRUD import Clientes, Criptografados, Descriptografados

class View:
    @staticmethod
    def inserir_cliente (ip):
        c = Cliente(0, ip)
        Clientes.inserir(c)

    @staticmethod
    def listar_clientes ():
        return Clientes.listar()
    
    @staticmethod
    def excluir_cliente (id):
        c = Clientes.buscar_por_id(id)
        Clientes.excluir(c)

    @staticmethod
    def atualizar_cliente (id, ip):
        c = Cliente(id, ip)
        Clientes.atualizar(c)

    @staticmethod
    def buscar_cliente_ip (ip):
        for cliente in Clientes.listar():
            if cliente.ip == ip:
                return cliente
        return None
    
    @staticmethod
    def buscar_cliente_id (id):
        for cliente in Clientes.listar():
            if cliente.id == id:
                return cliente
        return None

    @staticmethod
    def inserir_criptografado (id_cliente, mensagem_criptografada):
        c = Criptografado(0, id_cliente, mensagem_criptografada)
        Criptografados.inserir(c)
        return c

    @staticmethod
    def listar_criptografados ():
        return Criptografados.listar()
    
    @staticmethod
    def excluir_criptografado (id):
        c = Criptografados.buscar_por_id(id)
        Criptografados.excluir(c)

    @staticmethod
    def atualizar_criptografado (id, id_cliente, mensagem_criptografada):
        c = Criptografado(id, id_cliente, mensagem_criptografada)
        Criptografados.atualizar(c)

    @staticmethod
    def buscar_criptografado_id (id):
        for criptografado in Criptografados.listar():
            if criptografado.id == id:
                return criptografado
        return None

    @staticmethod
    def inserir_descriptografado (id_cliente, id_criptografado, cpu, mem, disk, temp):
        c = Descriptografado(0, id_cliente, id_criptografado, cpu, mem, disk, temp)
        Descriptografados.inserir(c)

    @staticmethod
    def listar_descriptografados ():
        return Descriptografados.listar()
    
    @staticmethod
    def excluir_descriptografado (id):
        c = Descriptografados.buscar_por_id(id)
        Descriptografados.excluir(c)

    @staticmethod
    def atualizar_descriptografado (id, id_cliente, cpu, mem, disk, temp):
        c = Descriptografado(id, id_cliente, cpu, mem, disk, temp)
        Descriptografados.atualizar(c)

    @staticmethod
    def buscar_descriptografado_id (id):
        for descriptografado in Descriptografados.listar():
            if descriptografado.id_criptografado == id:
                return descriptografado
        return None
    
    @staticmethod
    def buscar_descriptografado_id_cliente (id_cliente):
        descriptografados = []
        for descriptografado in Descriptografados.listar():
            if descriptografado.id_cliente == id_cliente:
                descriptografados.append(descriptografado)
        return descriptografados