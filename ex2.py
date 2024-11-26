class Quadrado():
    def __init__(self,medida):
        self.medida = medida

    def mostrar_area(self):
        self.area = self.medida **2
        print('Area:',self.area)

    def mudar_valor_lado(self):
        self.medida = float(input('Novo tamanho dos lados:'))
        print('A nova medida é:',self.medida)
        print('A nova area é:',self.medida**2)
        
quadrado = Quadrado(1)
quadrado.mostrar_area()
quadrado.mudar_valor_lado()