class Bola():
    def __init__ (self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self):
        self.cor = str(input('Nova cor:'))

    def mostra_cor(self):
        print('A nova cor é' ,self.cor)
        
bola = Bola('Rosa',30,'PVC')
print('Cor:',bola.cor)
bola.troca_cor()
bola.mostra_cor()