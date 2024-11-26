class Ponto():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class Retangulo():
    def __init__(self,largura,altura,vertice_inferior_esquerdo):
        self.largura = largura
        self.altura = altura
        self.vertice_inferior_esquerdo = vertice_inferior_esquerdo
    def encontrar_centro(self):
        centro_x = self.vertice_inferior_esquerdo.x + self.largura/2
        centro_y = self.vertice_inferior_esquerdo.y + self.altura/2
        return Ponto (centro_x,centro_y)
def imprimir_ponto(ponto):
    print(f'Cordenadas do ponto:{ponto}')
def menu():
    retangulos=[]
    while True:
        print('\nMenu:')
        print('1.Criar retangulo')
        print('2.Alterar valores')
        print('3.Encontrar e imprimir o centro')
        print('4.Lista todos os retangulos')
        print('5.Sair')
        opcao = int(input('Digite o que deseja:'))
    
        if opcao == 1:
            print('\nCriando retangulo...')
            largura = float(input('Digite a largura:'))
            altura = float(input('Digite a altura:'))
            x = float(input('Digite o x do vertice inferior esquerdo:'))
            y = float(input('Digite o y do vertice inferior esquerdo:'))
            ponto = Ponto(x,y)
            retangulo = Retangulo(largura,altura,ponto)
            retangulos.append(retangulo)
            print('Triangulo criado com sucesso!')
        
        if opcao == 2:
            if not retangulos:
                print('Nenhum triangulo cadastrado!')
                continue
        if opcao == 3:
            if not retangulos:
                print('Nenhum retangulo encontrado!')
            