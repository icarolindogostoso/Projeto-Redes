import json
from poo.model.cliente import Cliente
from poo.model.criptografado import Criptografado
from poo.model.descriptografado import Descriptografado

class CRUD:

    objetos = []

    @classmethod
    def inserir (cls, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id:
                id = x.id

        obj.id = id + 1

        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar (cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def buscar_por_id(cls, id):
        cls.abrir()
        for x in cls.objetos:
            if x.id == id:
                return x
        return None
    
    @classmethod
    def atualizar(cls, obj):
        x = cls.buscar_por_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()    
                
    @classmethod
    def excluir(cls, obj):
        x = cls.buscar_por_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()
            
    @classmethod
    def abrir():
        pass

    @classmethod
    def salvar():
        pass

class Clientes(CRUD):
    @classmethod    
    def salvar(cls):
        with open("Data/clientes.json", mode="w") as arquivo:
            dados = [aluno.to_dict() for aluno in cls.objetos]
            json.dump(dados, arquivo)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/clientes.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)

                for obj in objetos_json:
                    A = Cliente(obj["id"], obj["ip"])
                    cls.objetos.append(A)    

        except FileNotFoundError as e:
            raise ValueError (e)
        
class Criptografados (CRUD):
    @classmethod
    def salvar (cls):
        with open("Data/criptografados.json", mode="w") as arquivo:
            dados = [aluno.to_dict() for aluno in cls.objetos]
            json.dump(dados, arquivo)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/criptografados.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)

                for obj in objetos_json:
                    A = Criptografado(obj["id"], obj["id_cliente"], obj["msg"])
                    cls.objetos.append(A)    

        except FileNotFoundError as e:
            raise ValueError (e)
        
class Descriptografados (CRUD):
    @classmethod
    def salvar (cls):
        with open("Data/descriptografados.json", mode="w") as arquivo:
            dados = [aluno.to_dict() for aluno in cls.objetos]
            json.dump(dados, arquivo)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/descriptografados.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)

                for obj in objetos_json:
                    A = Descriptografado(obj["id"], obj["id_cliente"], obj["id_criptografado"], obj["cpu"], obj["mem"], obj["disk"], obj["temp"])
                    cls.objetos.append(A)    

        except FileNotFoundError as e:
            raise ValueError (e)