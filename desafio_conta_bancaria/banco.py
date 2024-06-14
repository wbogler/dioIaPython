class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def visualizar_extrato(self):
        print(f"Extrato da conta de {self.titular}:")
        for linha in self.extrato:
            print(linha)
        print(f"Saldo atual: R${self.saldo:.2f}")

# Exemplo de uso do sistema bancário
conta = ContaBancaria("João Silva", 1000)
conta.depositar(500)
conta.sacar(200)
conta.visualizar_extrato()