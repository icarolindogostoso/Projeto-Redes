import socket
from threading import Thread
from Crypto.Cipher import AES

class Servidor:
    def __init__ (self, ip: str, porta: int) -> None:
        """Inicialização do servidor com IP e porta"""
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4 e tcp
        self.ipPorta = (ip, porta)
        self.soc.bind(self.ipPorta)

    def decrypt(self, iv, enc_text):
        key = b'0361231230000000'
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        return cipher.decrypt(enc_text).decode("UTF-8")

    def client (self, conexao, docliente):
        """Lidar com a conexão de cada cliente"""
        print(f"O cliente {docliente} se conectou")

        testa_mensagem = ''

        while True: # loop para receber mensagnes do cliente
            mensagem_recebida = conexao.recv(1024).decode("utf-8")

            if not mensagem_recebida:
                break

            if testa_mensagem != mensagem_recebida:
                try:
                    print("Recebi =", mensagem_recebida, ", do cliente", docliente)

                    tupla = eval(mensagem_recebida)
                    iv = tupla[0]
                    enc_text = tupla[1]
                    dec_text = self.decrypt(iv, enc_text)
                    print(dec_text, "\n")
                    # print("Decifrada =", dec_text, ", do cliente", docliente, "\n")
                    # testa_mensagem = dec_text 
                except Exception as e:
                    print(e)

        conexao.close()

    def ligar(self) -> None:
        """Ligar o servidor e aceitar conexões
        
        a ideia por tras é que ele vai fazer treads simultaneas para que mais de uma pessoa
        possa se conectar ao mesmo tempo."""

        self.soc.listen(5) # numero maximo de conexoes pendentes

        while True: # loop principal para aceitar multiplas conexoes
            conexao, docliente = self.soc.accept() # aceita uma nova conexao

            thread_cliente = Thread(target=self.client, args=(conexao, docliente)) # cria uma nova thread para tratar a conexao do cliente
            thread_cliente.start()

def main():
    servidor = Servidor("0.0.0.0", 8000)
    servidor.ligar()

if __name__ == "__main__":
    main()