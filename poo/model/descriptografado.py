class Descriptografado:
    def __init__ (self, id, id_cliente, id_criptografado, cpu, mem, disk, temp):
        self.id = id
        self.id_cliente = id_cliente
        self.id_criptografado = id_criptografado
        self.cpu = cpu
        self.mem = mem
        self.disk = disk
        self.temp = temp

    def __str__ (self):
        return f"Informacoes coletadas: cpu: {self.cpu}, mem: {self.mem}, disk: {self.disk}, temp: {self.temp}"
    
    def to_dict (self):
        return {"id": self.id, "id_cliente": self.id_cliente, "id_criptografado": self.id_criptografado, "cpu": self.cpu, "mem": self.mem, "disk": self.disk, "temp": self.temp}
    
    @property
    def id(self):
        return self.__id
    
    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @property
    def id_criptografado(self):
        return self.__id_criptografado
    
    @property
    def cpu(self):
        return self.__cpu
    
    @property
    def mem(self):
        return self.__mem
    
    @property
    def disk(self):
        return self.__disk
    
    @property
    def temp(self):
        return self.__temp
    
    @id.setter
    def id(self, id):
        self.__id = id

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    @id_criptografado.setter
    def id_criptografado(self, id_criptografado):
        self.__id_criptografado = id_criptografado
    
    @cpu.setter
    def cpu(self, cpu):
        self.__cpu = cpu

    @mem.setter
    def mem(self, mem):
        self.__mem = mem

    @disk.setter
    def disk(self, disk):
        self.__disk = disk

    @temp.setter
    def temp(self, temp):
        self.__temp = temp