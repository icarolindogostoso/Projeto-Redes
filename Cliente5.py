import socket, time
from Sistema import Sistema

class Cliente:
    def __init__ (self, ip_servidor: str, porta_servidor: int):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.destino(ip_servidor, porta_servidor)

    def conectar(self):
        self.tcp.connect(self.destino)
        print(f"Conectado ao servidor {self.ip_servidor}:{self.porta_servidor}")

    def coletar_dados_sistema(self):
        qtd_cpu = Sistema.quantidade_processadores()
        memoria = Sistema.memoria_ram_livre()
        disco = Sistema.espaco_disco_livre()
        #temperatura = Sistema.temperatura_cpu()
        temperatura = 0

        mensagem = f"Quantidade de processadores lógicos: {qtd_cpu}\n" \
                   f"Quantidade de memória livre: {memoria} GB\n" \
                   f"Quantidade de espaço livre no disco: {disco} GB\n" \
                   f"Temperatura da CPU: {temperatura}°C"
        
        return mensagem
    
    def enviar_mensagem(self):
        mensagem = self.coletar_dados_sistema()
        self.tcp.send(bytes(mensagem, "utf-8"))
        print(f"Enviando: {mensagem}")

    def executar(self):
        while True:
            self.enviar_mensagem()
            time.sleep(15)

    def fechar_conexao(self):
        self.tcp.close()
        print("Conexão fechada.")

def main():
    cliente = Cliente('10.25.1.81', 8000)
    cliente.conectar()
    try:
        cliente.executar()
    except KeyboardInterrupt:
        cliente.fechar_conexao()

if __name__ == "__main__":
    main()