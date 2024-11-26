class Pessoa():
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade 
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.saver = self.idade
        self.idade = int(input('Nova idade:'))

    def crescer(self):
        if self.idade <= 21:
            for i in range(self.idade - self.saver):
                self.altura = self.altura + 0.05
        print(f'A nova altura:',self.altura)

pessoa = Pessoa('Anne',17,65,1.63)
pessoa.envelhecer()
pessoa.crescer()
    