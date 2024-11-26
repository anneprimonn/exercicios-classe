class Retangulo():
    def __init__(self,base,altura):
        self.base = base
        self.base = base
        self.altura = altura

    def mudar_valor_lado(self):
        self.base = float(input('Nova base:'))
        self.altura = float(input('Nova altura:'))

    def valor_lado(self):
        print(f'O novo valor da base é {self.base} e a nova alyura é {self.altura}') 

    def calcular_area(self,pisos):
        self.area = 2* (self.base + self.altura)
        print(f'A area é {self.area} e a quantidade de pisos é {self.area / pisos}')  

    def calcular_perimetro(self,rodape):
        self.perimetro = self.base + self.altura   
        print(f'O perimetreo é {self.perimetro} e a quantidade para o rodapé é {self.perimetro / rodape}')

local = Retangulo(7,7)
piso = 2
local.calcular_area(piso)
rodape = 2
local.calcular_perimetro(rodape)