#Forçar a ler apenas números inteiros
def leiaInt(msg):
    while True:
        try:
            entrada = str(input(msg))
            if entrada.strip() == '':
                return 0
            if '.' in entrada or ',' in entrada:
                print('Float não')
                continue
            num = int(entrada)
        except ValueError:
            print('Letras não funcionam só números inteiros')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida')
            return 0
        except Exception as erro:
            print(f'O erro que ocorreu foi {erro.__class__}')
            continue
        else:
            return num


#Forçar o sexo ser apenas M ou F ou N/I
def leiaSexo(msg):
    while True:
        sexo = str(input(msg))
        if sexo.strip() == '':
            return 'N/I'
        if sexo.isalpha():
            if sexo in 'MmFf':
                return sexo.upper()
        else:
            print('Somente [M/F]')


#Padronizar linhas e títulos
def linha():
    print('-' * 50)


def titulo(msg):
    cor = cores()
    print(cor[2])
    linha()
    print(msg.center(50))
    linha()
    print(cor[0])


#Facilitar o Uso das cores
def cores():
    return {
        0: '\033[m',     #Sem cor
        1: '\033[0;31m', #Vermelho
        2: '\033[0;32m', #Verde
        3: '\033[0;33m', #Amarelo
        4: '\033[0;34m', #Azul
        5: '\033[0;35m', #Roxo
        6: '\033[0;36m', #Ciano
        7: '\033[0;37m'} #Cinza


#Criação de um menu com escolhas
def menu(lista):
    cor = cores()
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cor[3]}{c}{cor[0]} - {cor[2]}{item}{cor[0]}')
        c += 1
    print(cor[2])
    linha()
    print(cor[0])
    opc = leiaInt('Sua Opção: ')
    return opc


#Verificar se o arquivo ja existe e caso não exista irá criar um usando o def criarArquivo
def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um erro na criaçaõ do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


#Exibir a lista de nomes registrados
def lerArquivo(nome):
    cor = cores()
    try:
        arquivo = open(nome, 'rt')
        linhas = arquivo.readlines() #Copia do arquivo para segurança, podendo encerrar o arquivo em seguida e usar somente a copia
        arquivo.close()
    except:
        print('Erro ao ler o arquivo.')
    else:
        titulo('PESSOAS CADASTRADAS'.center(30))
        print(f'{cor[3]}{"ID"}  {"NOME":<20}{"IDADE":>6}{"SEXO":>8}{"ESTADO":>10}{cor[0]}')
        linhas_ordenadas = sorted(linhas, key=lambda l: l.split(';')[1].strip().lower())
        for dado in linhas_ordenadas:
            dado = dado.strip().split(';')
            if len(dado) < 5:
                continue
            print(f'{cor[3]}{dado[0]:<4}{cor[0]}{dado[1].title():<20}{dado[2]:<9}{dado[3]:<8}{dado[4].upper()}')


#Registrar novos usuários
def registrar(arq, nome='Desconhecido', idade=0, sexo='N/I', estado='N/I'):
    if nome == '':
        nome = 'Desconhecido'
    if estado == '':
        estado = 'N/I'
    novoID = ordemID(arq)
    try:
        arquivo = open(arq, 'at')
    except:
        print('Erro no acesso ao arquivo.')
    else:
        try:
            arquivo.write(f'{novoID};{nome}; {idade}; {sexo}; {estado}\n')
        except:
            print('Erro ao registrar pessoa.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            arquivo.close()


#Ordenar o ID e registrar junto com os nomes
def ordemID(arq):
    try:
        arquivo = open(arq, 'rt')
        linhas = arquivo.readlines()
        arquivo.close()
    except:
        return 1
    if not linhas:
        return 1
    maior = 0
    for linha in linhas:
        partes = linha.strip().split(';')
        if partes[0].isdigit():
            if int(partes[0]) > maior:
                maior = int(partes[0])
    return maior + 1


#Remover usuário
def remover(arq, id_remover):
    if id_remover == 0:
        return
    try:
        arquivo = open(arq, 'rt')
        linhas = arquivo.readlines()
        arquivo.close()
        indice = id_remover - 1
        for i, linha in enumerate(linhas):
            partes = linha.strip().split(';')
            if partes[0].isdigit() and int(partes[0]) == id_remover:
                indice = i
                break
        if indice != -1:
            remover = linhas.pop(indice)
            arquivo = open(arq, 'wt')
            arquivo.writelines(linhas)
            arquivo.close()
            print(f'O cadastro de {remover.split(";")[1]} foi removido com sucesso.')
        else:
            print('ID Inválido')
    except Exception as erro:
        print(f'O Erro que ocorreu foi {erro.__class__}')
    finally:
        if arquivo and not arquivo.closed:
            arquivo.close()

