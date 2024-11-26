class TV():
    def __init__(self):
        self.n_canal = 0
        self.n_volume = 0

    def volume_aumen_dimin(self):
        self.n_volume = int(input('Digite o volume:'))
        if self.n_volume > 10:
            print('Volume máximo é 10')
            self.n_volume = 10
        else:
            print(f'Volume ajustado para {self.n_volume}')
    
    def mudar_canal(self):
        self.n_canal = int(input('Digite o canal:'))
        if self.n_canal >= 30:
            print('limite maximo de canais')
        if self.n_canal == 0:
            print('limite maximo de canais')
        else:
            print(f'Canal modificado para {self.n_canal}')

opcao = TV()
opcao.volume_aumen_dimin()
opcao.mudar_canal()
