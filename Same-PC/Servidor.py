import socket

class Servidor:
    def __init__(self, host: str, porta: int) -> None:
        self.host = host
        self.porta = porta
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria uma conexao ipv4 e tco
        self.servidor.bind((self.host, self.porta))
        self.servidor.listen()

    def aguardar_conexoes(self) -> None:
        print("Servidor aguardando conexão...")
        while True:
            cliente, endereco = self.servidor.accept()
            print(f"Conexão de {endereco} estabelecida.")
            self.processar_cliente(cliente)

    def processar_cliente(self, cliente) -> None:
        dados = cliente.recv(1024).decode()
        print(f"Dados recebidos: {dados}")
        cliente.close()

def main():
    servidor = Servidor('localhost', 50000)
    servidor.aguardar_conexoes()

if __name__ == "__main__":
    main()
