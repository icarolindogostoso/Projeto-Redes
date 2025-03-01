import socket
from threading import Thread, Lock
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import time
import json

class Servidor:
    def __init__ (self, ip: str, porta: int) -> None:
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ipPorta = (ip, porta)
        self.soc.bind(self.ipPorta)
        self.clientes = {}
        self.lock = Lock()

    def decrypt(self, iv, enc_text):
        key = b'0361231230000000'
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        decrypted_padded_message = cipher.decrypt(enc_text)
        decrypted_message = unpad(decrypted_padded_message, AES.block_size)
        return decrypted_message.decode("UTF-8")

    def client (self, conexao, docliente):
        print(f"O cliente {docliente} se conectou")

        while True:
            mensagem_recebida = conexao.recv(1024).decode("utf-8")

            if not mensagem_recebida:
                break

            if mensagem_recebida == 'get_data':
                with self.lock:
                    dados = json.dumps(self.clientes)

                conexao.sendall(dados.encode("utf-8"))
                continue

            try:
                print("Recebi =", mensagem_recebida, ", do cliente", docliente)

                tupla = eval(mensagem_recebida)
                iv = tupla[0]
                enc_text = tupla[1]
                dec_text = self.decrypt(iv, enc_text)
                dados_cliente = json.loads(dec_text)

                with self.lock:
                    self.clientes[docliente] = dados_cliente

                print(dec_text, "\n")
            except Exception as e:
                print(e)

        conexao.close()

    def broadcast_server_ip(self):
        interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
        allips = [ip[-1][0] for ip in interfaces]
        msg = str(self.ipPorta).encode("utf-8")
        while True:
            for ip in allips:
                print(f'Publicando em {ip}')
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                sock.bind((ip,0))
                sock.sendto(msg, ("255.255.255.255", 5005))
                sock.close()
            time.sleep(5)

    def ligar(self) -> None:
        self.soc.listen(5)

        broadcast_thread = Thread(target=self.broadcast_server_ip, daemon=True)
        broadcast_thread.start()

        while True:
            conexao, docliente = self.soc.accept()

            thread_cliente = Thread(target=self.client, args=(conexao, docliente))
            thread_cliente.start()

def main():
    servidor = Servidor("0.0.0.0", 8000)
    servidor.ligar()

if __name__ == "__main__":
    main()