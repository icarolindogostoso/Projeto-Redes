import socket, time
from Sistema import Sistema

class Cliente:
    def __init__(self, porta_servidor: int):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.porta_servidor = porta_servidor
        self.ip_servidor = None

    def conectar(self):
        # Conecta-se a qualquer servidor para receber o IP
        self.tcp.bind(('0.0.0.0', 0))  # Escolhe uma porta disponível
        self.tcp.connect(('127.0.0.1', self.porta_servidor))  # Conecta ao servidor para pegar o IP
        print("Conectado ao servidor para receber o IP...")

        # Espera a resposta com o IP do servidor
        self.ip_servidor = self.tcp.recv(1024).decode('utf-8')
        print(f"IP do servidor recebido: {self.ip_servidor}")
        self.tcp.close()  # Fecha a primeira conexão, pois já pegou o IP

    def coletar_dados_sistema(self):
        qtd_cpu = Sistema.quantidade_processadores()
        memoria = Sistema.memoria_ram_livre()
        disco = Sistema.espaco_disco_livre()
        temperatura = 0  # Ou use a função real se disponível

        mensagem = f"Quantidade de processadores lógicos: {qtd_cpu}\n" \
                   f"Quantidade de memória livre: {memoria} GB\n" \
                   f"Quantidade de espaço livre no disco: {disco} GB\n" \
                   f"Temperatura da CPU: {temperatura}°C"
        
        return mensagem
    
    def enviar_mensagem(self):
        if self.ip_servidor:
            # Agora o cliente sabe o IP do servidor
            self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp.connect((self.ip_servidor, self.porta_servidor))
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
    cliente = Cliente(8000)  # Porta do servidor
    cliente.conectar()
    try:
        cliente.executar()
    except KeyboardInterrupt:
        cliente.fechar_conexao()

if __name__ == "__main__":
    main()
