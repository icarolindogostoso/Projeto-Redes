import socket
from threading import Thread
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import time

class Servidor:
    def __init__ (self, ip: str, porta: int) -> None:
        """Inicialização do servidor com IP e porta"""
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 e TCP
        self.ipPorta = (ip, porta) # Ip e porta do servidor
        self.soc.bind(self.ipPorta)

    def decrypt(self, iv, enc_text):
        """Decodifica a mensagem criptografada"""
        key = b'0361231230000000'# Chave que vai ser usada para criptografar e descriptografar
        cipher = AES.new(key, AES.MODE_CBC, iv=iv) # Cria um novo objeto de criptografia, com a chave, o modo de operacao (CBC) e o vetor de inicalizacao
        decrypted_padded_message = cipher.decrypt(enc_text) # Mensagem descriptografada com 16 bytes
        decrypted_message = unpad(decrypted_padded_message, AES.block_size) # Mensagem descriptografada sem preenchimento, precisando saber a mensagem e qual o seu preenchimento (AES.block_size = 16 bytes)
        return decrypted_message.decode("UTF-8")

    def client (self, conexao, docliente):
        """Lidar com a conexão de cada cliente"""
        print(f"O cliente {docliente} se conectou")

        while True: # Loop para receber mensagnes do cliente
            mensagem_recebida = conexao.recv(1024).decode("utf-8")

            if not mensagem_recebida: # Caso a conexão seja fechada
                break

            try:
                print("Recebi =", mensagem_recebida, ", do cliente", docliente)

                tupla = eval(mensagem_recebida) # A mensagem recebida vem como uma tupla com o iv e o texto encriptado
                iv = tupla[0]
                enc_text = tupla[1]
                dec_text = self.decrypt(iv, enc_text) # Processo de descriptografia
                print(dec_text, "\n")
            except Exception as e:
                print(e)

        conexao.close()

    def broadcast_server_ip(self):
        """Manda o ip e a porta do servidor para todos os clientes"""
        interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET) # Obtem todas as interfaces de rede do computador
        allips = [ip[-1][0] for ip in interfaces] # Obtem todos os IPs das interfaces de rede do computador
        msg = str(self.ipPorta).encode("utf-8")
        while True:
            for ip in allips: # Para cada IP
                print(f'Publicando em {ip}')
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Habilita o envio de pacotes de broadcast
                sock.bind((ip,0))
                sock.sendto(msg, ("255.255.255.255", 5005)) # Envia a mensagem com o ip e a porta do servidor para todos que estão na mesma rede do IP
                sock.close()
            time.sleep(5)

    def ligar(self) -> None:
        """Ligar o servidor e aceitar conexões
        
        a ideia por tras é que ele vai fazer treads simultaneas para que mais de uma pessoa
        possa se conectar ao mesmo tempo."""

        self.soc.listen(5) # Numero maximo de conexoes pendentes

        broadcast_thread = Thread(target=self.broadcast_server_ip, daemon=True) # Thread para ficar sempre publicando o ip e a porta do servidor caso mais alguem queira se conectar
        broadcast_thread.start()

        while True: # Loop principal para aceitar multiplas conexoes
            conexao, docliente = self.soc.accept() # Aceita uma nova conexao

            thread_cliente = Thread(target=self.client, args=(conexao, docliente)) # Cria uma nova thread para tratar a conexao do cliente
            thread_cliente.start()

def main():
    servidor = Servidor("0.0.0.0", 8000)
    servidor.ligar()

if __name__ == "__main__":
    main()