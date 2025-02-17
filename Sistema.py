import psutil, wmi

class Sistema:
    def __init__ (self) -> None:
        pass
    
    def quantidade_processadores (self) -> int:
        """Quantidade de processadores lógicos no sistema"""
        return psutil.cpu_count(logical=True)
    
    def memoria_ram_livre (self) -> int:
        """Quantidade de memória livre em GB"""
        memoria = psutil.virtual_memory()
        return round(memoria.available / (1024 ** 3), 2) # converter em GB
    
    def espaco_disco_livre (self) -> int:
        """Quantidade de espaço livre em GB"""
        disco = psutil.disk_usage("c:\\")
        return round(disco.free / (1024 ** 3), 2) # converter em GB
    
    def temperatura_cpu (self):
        """Temperatura da CPU em graus Celsius"""
        temperaturas = psutil.sensors_temperatures()

        if "coretemp" in temperaturas:
            cpu_temps = temperaturas["coretemp"]
            return cpu_temps[0].current
        else:
            return 0
        
sistema = Sistema()

print(f"Quantidade de processadores: {sistema.quantidade_processadores()}")
print(f"Memoria RAM livre: {sistema.memoria_ram_livre()} GB")    
print(f"Espaco de disco livre: {sistema.espaco_disco_livre()} GB")
print(f"Temperatura da CPU: {sistema.temperatura_cpu()} °C")