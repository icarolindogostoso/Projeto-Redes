class Cliente:
    def __init__ (self, id, ip):
        self.id = id
        self.ip = ip

    def __str__(self):
        return f"IP do cliente: {self.ip}"
    
    def to_dict(self):
        return {"id": self.id, "ip": self.ip}
    
    @property
    def id(self):
        return self.__id
    
    @property
    def ip(self):
        return self.__ip
    
    @id.setter
    def id(self, id):
        self.__id = id

    @ip.setter
    def ip(self, ip):
        self.__ip = ip