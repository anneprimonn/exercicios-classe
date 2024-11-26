class ContaCorrente():
    def __init__(self,conta,nome,saldo):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self):
        self.nome = str(input('Novo nome:'))

    def deposito(self):
        dep = float(input('Valor do deposito:'))
        self.saldo += dep

    def saque(self):
        saq = float(input('Valor do saque:'))
        self.saldo -= saq

conta = ContaCorrente(1234, 'Anne', 500)
conta.alterar_nome()
conta.deposito()
conta.saque()
print(conta.alterar_nome)
print('Saldo:',conta.saldo)