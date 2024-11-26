#encapsulamento (usar _ _ antes para nao ter acessoa aquela info)

class encapsulamento():
    def __init__ (self,n1,n2):
        self.__n1 = n1
        self.__n2 = n2
    def adicionar(self):
        return self.__n1 + self.__n2
calc = encapsulamento(20,10)
print(calc.adicionar())
calc.__n1

