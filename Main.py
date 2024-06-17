
class Transacao:
    def __init__(self, valor):
        self.valor = valor

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Cliente:
    def __init__(self, agencia, endereco):
        self.agencia = agencia
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0
        self.historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        self.historico.adicionar_transacao(Transacao(valor))

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.adicionar_transacao(Transacao(-valor))
            return True
        return False