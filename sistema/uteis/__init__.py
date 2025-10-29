def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um numero valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO Usuario preferiu não digitar.\033[m')
            return 0
        else:
            return n
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um numero valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO Usuario preferiu não digitar.\033[m')
            return 0
        else:
            return n
        
def verificarLista(lista, msg= 'ERRO! NÃO A NENHUM PRODUTO'):
    try:
        a = lista[0]
    except IndexError:
        print(f'\033[31m{msg}\033[m')
        return False
    else:
        return True

def leiaOpc(msg, lista):
    opc = input(msg)
    for p in lista:
        if opc == p['nome_do_produto']:
            opc = p['nome_do_produto']
            return True
        else:
            print('\033[31mERRO! OPÇÃO NÃO EXISTENTE\033[m')
            return False

def validacaoOpc(msg):
    try:
        opc = input(msg).upper()
    except KeyboardInterrupt:
        print('\033[31mNENHUMA OPÇÃO ESCOLHIDA\033[m')
        return 0
    else:
        return opc
