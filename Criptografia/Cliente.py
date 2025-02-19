import socket, time
from Sistema import Sistema
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

class Cliente:
    def __init__ (self, ip_servidor: str, porta_servidor: int):
        self.ip_servidor = ip_servidor
        self.porta_servidor = porta_servidor
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.destino = (ip_servidor, porta_servidor)

    def encrypt (self, message):
        key = b'0361231230000000'
        cipher = AES.new(key, AES.MODE_CBC)
        b = message.encode("UTF-8")
        b_padded = pad(b, AES.block_size)
        return cipher.iv, cipher.encrypt(b_padded)

    def conectar(self):
        self.tcp.connect(self.destino)
        print(f"Conectado ao servidor {self.ip_servidor}:{self.porta_servidor}")

    def coletar_dados_sistema(self):
        qtd_cpu = Sistema.quantidade_processadores()
        memoria = Sistema.memoria_ram_livre()
        disco = Sistema.espaco_disco_livre()
        #temperatura = Sistema.temperatura_cpu()
        temperatura = 0

        return qtd_cpu, memoria, disco, temperatura
    
    def enviar_mensagem(self):
        qtd_cpu, memoria, disco, temperatura = self.coletar_dados_sistema()

        dados = {
            "cpu": qtd_cpu,
            "mem": memoria,
            "disk": disco,
            "temp": temperatura
        }

        def encriptar_e_enviar(identificador, valor):
            mensagem = f"{identificador}: {valor}"
        
            iv, enc_msg = self.encrypt(mensagem)
            
            msg_env = str((iv, enc_msg))
            self.tcp.send(bytes(msg_env, "utf-8"))
            
            print(f"Enviando: {mensagem}")
            print(f"Criptografada: {msg_env}")

        for identificador, valor in dados.items():
            encriptar_e_enviar(identificador, valor)
            print("")

    def executar(self):
        while True:
            self.enviar_mensagem()
            time.sleep(15)

    def fechar_conexao(self):
        self.tcp.close()
        print("Conexão fechada.")

def main():
    cliente = Cliente('26.9.174.145', 8000)
    cliente.conectar()
    try:
        cliente.executar()
    except KeyboardInterrupt:
        cliente.fechar_conexao()

if __name__ == "__main__":
    main()
