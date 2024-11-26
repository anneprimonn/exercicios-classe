class Conta():
    def __init__ (self,nome,saldo,cpf,senha):
        self.nome = nome
        self.__saldo = saldo
        self.__cpf = cpf
        self.__senha = senha
     
    def extrato(self,senha):
        if senha == self.__senha:
            print(f'Saldo: {self.__saldo}')
        else:
            print('Senha invalida!')

    def depositar(self,valor):
        self.__saldo += valor
    
    def sacar(self,senha,valor):
        if senha == self.__senha:
            self.__saldo -= valor
        else:
            print('Senha invalida!')
            
while True:
    print('\n1.Cadastro')
    print('2.Saldo')
    print('3.Saque')
    print('4.Deposito')
    opcao = int(input('Digite oque deseja:'))

    if opcao == 1:
        nome = str(input('\nNome: '))
        cpf = int(input('Digite o CPF (apenas numeros): '))
        senha = int(input('Senha (apenas numeros): '))
        conta = Conta(nome,0, cpf,senha)
    
    elif opcao == 2:
        senha = int(input('Senha (apenas numeros): '))
        conta.extrato(senha)

    elif opcao == 3:
        senha = int(input('Senha (apenas numeros): '))
        valor = float(input('Digite o saque: '))
        conta.sacar(senha,valor)
        print('Saque efetuado com sucesso!')
    
    elif opcao == 4:
        valor = float(input('Digite o valor para depositar:'))
        conta.depositar(valor)
        print('Deposito efetuado com sucesso!')