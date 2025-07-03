from ex115.lib.interface import *

def arquivoExiste(nome):
    """
    --> função para verificar se axiste algum arquivo de texto.
    :param nome: verifica se existe algum arquivo de texto criado no app.
    :return: retorna uma resposta positiva ou erro na ausencia do texto.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    --> cria um arquivo de texto que serve como banco de dados, para nome e idade.
    :param nome: nome do usuario para inserir no arquivo de texto.
    :return: retorna uma menssagem positiva ou negativa.
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    """
    --> le o arquivo de texto gerado para cadastro de nome e idade de usuario.
    :param nome: nome do usuario.
    :return: retorna uma resposta positiva ou negativa.
    """
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    """
    --> função para cadastrar o usuario no arquivo de texto criado.
    :param arq: variavel arquivo, para cadastro.
    :param nome: nome do usuario.
    :param idade: idade do usuario.
    :return: retorna uma menssagem positiva ou negativa.
    """
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('houve um ERRO na hora de escrever os dados!')
        else:
            print(f'novo registro de {nome} adicionado com sucesso!')
            a.close()