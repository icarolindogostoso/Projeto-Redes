import psutil

class Sistema:
    @staticmethod
    def quantidade_processadores () -> int:
        """Quantidade de processadores lógicos no sistema"""
        return psutil.cpu_count(logical=True)
    
    @staticmethod
    def memoria_ram_livre () -> int:
        """Quantidade de memória livre em GB"""
        memoria = psutil.virtual_memory()
        return round(memoria.available / (1024 ** 3), 2)
    
    @staticmethod
    def espaco_disco_livre () -> int:
        """Quantidade de espaço livre em GB"""
        disco = psutil.disk_usage("C:\\")
        return round(disco.free / (1024 ** 3), 2) 
    
    @staticmethod
    def temperatura_cpu ():
        """Temperatura da CPU em graus Celsius (não está funcionando ainda)"""
        try:
            temperaturas = psutil.sensors_temperatures()
            if "coretemp" in temperaturas:
                cpu_temps = temperaturas["coretemp"]
                celsius = [(temp.current - 273.15) for temp in cpu_temps]
                return celsius
            else:
                return []
        except Exception as e:
            pass
        
        
# sistema = Sistema()

# print(f"Quantidade de processadores: {sistema.quantidade_processadores()}")
# print(f"Memoria RAM livre: {sistema.memoria_ram_livre()} GB")    
# print(f"Espaco de disco livre: {sistema.espaco_disco_livre()} GB")
# #print(f"Temperatura da CPU: {sistema.temperatura_cpu()} °C")
