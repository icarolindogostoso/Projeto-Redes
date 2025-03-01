import socket
import time
from Sistema import Sistema
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

class Cliente:
    @staticmethod
    def encrypt(message):
        """Encripta uma mensagem"""
        key = b'0361231230000000' # Chave que vai ser usada para criptografar e descriptografar
        cipher = AES.new(key, AES.MODE_CBC) # Cria um novo objeto de criptografia, com a chave, o modo de operacao (CBC)
        b = message.encode("UTF-8") # Mensagem a ser criptografada
        b_padded = pad(b, AES.block_size) # Mensagem criptografada com 16 bytes
        return cipher.iv, cipher.encrypt(b_padded) # Retorna o vetor de inicalizacao e a mensagem criptografada

    @staticmethod
    def coletar_dados_sistema():
        """Coleta os dados do sistema"""
        qtd_cpu = Sistema.quantidade_processadores()
        memoria = Sistema.memoria_ram_livre()
        disco = Sistema.espaco_disco_livre()
        #temperatura = Sistema.temperatura_cpu()
        temperatura = 0

        return f"cpu: {qtd_cpu}, mem: {memoria}, disk: {disco}, temp: {temperatura}"

    @staticmethod
    def buscar_conexao():
        """Busca uma conexao com um servidor"""
        print("Esperando servidores...")
        HOST = ''              # Endereco IP do Servidor
        PORT = 5005            # Porta que o Servidor esta
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        orig = (HOST, PORT)
        udp.bind(orig)
        while True:
            msg, cliente = udp.recvfrom(1024)
            tupla = eval(msg.decode("utf-8")) # A mensagem recebida vem como uma tupla com ip e porta

            return cliente[0], int(tupla[1]) # Retorna o ip e a porta

    @staticmethod
    def setar_conexao(ip, porta):
        """Seta uma conexao com um servidor"""
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 e TCP
        destino = (ip, porta) # Ip e porta do servidor
        return tcp, destino

    @staticmethod
    def conectar(tcp, destino):
        """Conecta ao servidor"""
        tcp.connect(destino)
        print(f"Conectado ao servidor {destino[0]}:{destino[1]}")

    @staticmethod
    def enviar_mensagem(tcp):
        """Envia uma mensagem ao servidor"""
        mensagem = Cliente.coletar_dados_sistema()

        iv, enc_msg = Cliente.encrypt(mensagem) # Processo de criptografia
        msg_env = str((iv, enc_msg))
        tcp.send(bytes(msg_env, "utf-8"))

        print(f"Enviando: {mensagem}")
        print(f"Criptografada: {msg_env}\n")

    @staticmethod
    def executar(tcp):
        """Executa o programa"""
        while True:
            Cliente.enviar_mensagem(tcp)
            time.sleep(5)

    @staticmethod
    def fechar_conexao(tcp):
        """Fecha a conexao"""
        tcp.close()
        print("Conexão fechada.")

def main():
    ip, porta = Cliente.buscar_conexao()
    tcp, destino = Cliente.setar_conexao(ip, porta)
    Cliente.conectar(tcp, destino)
    try:
        Cliente.executar(tcp)
    except KeyboardInterrupt:
        Cliente.fechar_conexao(tcp)

if __name__ == "__main__":
    main()