class Super():
    def __init__(self):
        self.nome = str(input('Nome:'))
        self.endereco = str(input('Endereço:'))
        self.cep = int(input('CEP:'))
        self.telefone = int(input('Telefone:'))
        self.email = str(input('Email:'))
        self.cor = str(input('Cor:'))
        self.civil = str(input(('Estado civil:')))
        self.proficao = str(input('Profição'))
class PessoaFisica(Super):
    def __init__(self):
        super().__init__()
        self.rg = int(input('RG:'))
        self.cpf = int(input('CPF:'))
        self.d_nascimento = str(input('Data de nascimento:'))
        self.genero = str(input('Genero:'))
        self.cnh = int(input('CNH:'))
class PessoaJuridica(Super):
    def __init__(self):
        super().__init__()
        self.n_empresa = str(input('Nome da empresa:'))
        self.abertura_empresa = int(input('Data de abertura da empresa:'))
        self.cpf = int(input('CPF:'))
        self.porte = str(input('Porte da empresa:'))
        self.n_inscricao = int(input('Numero de inscrição:'))
