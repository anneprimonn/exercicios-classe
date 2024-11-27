class Account(): #superclasse
    #number: numero da conta,holder: proprietario, balance: saldo

    def __init__(self,number: int,holder: str,balance: float):
        self.number = number
        self.holder = holder
        self.balance = balance

    def depost(self):
        value = float(input('Enter the amount to deposit:'))
        self.balance += value
        print(self.balance)

    def withdraw(self):
        value = float(input('Enter the amount to withdraw:'))
        if  value < self.balance:
            self.balance -= value
            print('successfully carried out')
        else:
            print('Insuficiente')


class BussinesAccount(Account): #herança

    def __init__(self, number: int, holder: str, balance: float, loanlimit: float):
        super().__init__(number, holder, balance)
        self.loanlimit = loanlimit

    def loan(self):
        value = float(input('Enter the loan amount:'))
        if value > self.loanlimit:
            print('Loan refused!')
        else:
            print('Loan completed!')