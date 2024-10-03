import hashlib
import time

class Bloco:
    def __init__(self, indice, dados, timestamp, hash_anterior):
        self.indice = indice
        self.dados = dados
        self.timestamp = timestamp
        self.hash_anterior = hash_anterior
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        valor = str(self.indice) + str(self.dados) + str(self.timestamp) + str(self.hash_anterior)
        return hashlib.sha256(valor.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.criar_bloco(inicial=True)

    def criar_bloco(self, dados=None, inicial=False):
        indice = len(self.chain) + 1
        timestamp = time.time()
        hash_anterior = "0" if inicial else self.chain[-1].hash
        novo_bloco = Bloco(indice, dados, timestamp, hash_anterior)
        self.chain.append(novo_bloco)
        return novo_bloco

    def adicionar_bloco(self, dados):
        return self.criar_bloco(dados)

    def visualizar_chain(self):
        for bloco in self.chain:
            print(f'Índice: {bloco.indice}, Dados: {bloco.dados}, Timestamp: {bloco.timestamp}, Hash Anterior: {bloco.hash_anterior}, Hash: {bloco.hash}')

# Uso da aplicação
blockchain = Blockchain()
blockchain.adicionar_bloco("Transação 1")
blockchain.adicionar_bloco("Transação 2")
blockchain.visualizar_chain()