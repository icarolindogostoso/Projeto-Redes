class Criptografado:
    def __init__ (self, id, id_cliente, msg):
        self.id = id
        self.id_cliente = id_cliente
        self.msg = msg

    def __str__ (self):
        return f"Mensagem recebida: {self.msg}"
    
    def to_dict (self):
        return {"id": self.id, "id_cliente": self.id_cliente, "msg": self.msg}
    
    @property
    def id(self):
        return self.__id
    
    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @property
    def msg(self):
        return self.__msg
    
    @id.setter
    def id(self, id):
        self.__id = id

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente
    
    @msg.setter
    def msg(self, msg):
        self.__msg = msg