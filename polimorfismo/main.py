from dados import PessoaFisica,PessoaJuridica
print('1.Pessoa Fisica')
print('2.Pessoa Juridica')
opcao = int(input('Digite 1 ou 2:'))

if opcao == 1:
    pessoa = PessoaFisica()
elif opcao == 2:
    pessoa = PessoaJuridica()

