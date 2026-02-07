from time import sleep
from dados.dados_cadastro.utils import *

#Criar um arquivo caso ele não exista
arq = 'sistemaCadastro.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

#Programa Principal
while True:
    cor = cores()
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Remover cadastro', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
        sleep(1)
    elif resposta == 2:
        titulo('CADASTRAR PESSOAS')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        sexo = leiaSexo('Sexo [M/F]: ')
        estado = str(input('Estado: '))
        registrar(arq, nome, idade, sexo, estado)
        sleep(1)
    elif resposta == 3:
        lerArquivo(arq)
        id_deletar = leiaInt('Digite o ID do usuário que deseja deletar [0 Encerra a ação]: ')
        remover(arq, id_deletar)
        sleep(1)
    elif resposta == 4:
        print('Saindo do sistema...')
        sleep(1)
        break
    else:
        print(f'{cor[1]}Opc Invalida{cor[0]}')
