import socket
from Sistema import Sistema
import time

class Cliente:
    def __init__(self, host: str, porta: int) -> None:
        self.host = host
        self.porta = porta

    def pegar_informacoes(self) -> str:
        qtd_cpu = Sistema.quantidade_processadores()
        memoria = Sistema.memoria_ram_livre()
        disco = Sistema.espaco_disco_livre()
        #temperatura = Sistema.temperatura_cpu()
        temperatura = 0
        return f"Quantidade de processadores lógicos: {qtd_cpu}\nQuantidade de memória livre: {memoria} GB\nQuantidade de espaço livre no disco: {disco} GB\nTemperatura da CPU: {temperatura}°C"

    def conectar_e_enviar(self) -> None:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            cliente.connect((self.host, self.porta))
            informacoes = self.pegar_informacoes()
            cliente.send(informacoes.encode())
            print(informacoes)
        except Exception as e:
            print(f"Erro ao conectar ao servidor: {e}")
        finally:
            cliente.close()

def main():
    cliente = Cliente('127.0.0.1', 50000)
    for _ in range(5):
        cliente.conectar_e_enviar()
        time.sleep(10)

if __name__ == "__main__":
    main()
