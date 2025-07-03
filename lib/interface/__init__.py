def leiaInt(msg):
    """
    --> função INPUT, para recebimento de dados pelo teclado do usuario.
    :param msg: menssagem do sistema.
    :return: retorna uma um valor ou erro.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um número válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar!')
            return 0
        else:
            return n

def linha(tam=42):
    """
    --> função para estilização e organização da interface.
    :param tam: tamanho da divisão.
    :return: retorna o valor da função.
    """
    return  '-' * tam

def cabeçalho(txt):
    """
    --> função cabeçalho, estilização da interface.
    :param txt: texto a ser exibido no inicio do app.
    :return: retorna um valor da função.
    """
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    """
    --> função menu, utilizado para a organização do menu inicial.
    :param lista: cria uma lista para organizar e alinhar os valores.
    :return: retorna um valor da função.
    """
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc