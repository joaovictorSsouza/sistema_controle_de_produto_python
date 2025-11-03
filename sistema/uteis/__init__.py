import pandas as pd
import os



def leiaInt(msg):
    '''Função para tratamento de erro caso a resposta não seja um numero'''
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
    '''Função para tratamento de erro caso a resposta não seja um numero float'''

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

def leiaOpc(msg, lista):
    '''Função para tratamento de erro caso a resposta não seja uma das opções da lista'''
    opc = input(msg)
    for p in lista:
        if opc == p['nome_do_produto']:
            opc = p['nome_do_produto']
            return True
        else:
            print('\033[31mERRO! OPÇÃO NÃO EXISTENTE\033[m')
            return False

def validacaoOpc(msg):
    '''Função para tratamento de erro caso a opção nao tenha sido digitada'''
    try:
        opc = input(msg).upper()
    except KeyboardInterrupt:
        print('\033[31mNENHUMA OPÇÃO ESCOLHIDA\033[m')
        return 0
    else:
        return opc

def verificar_produtos():
    '''Função para verificar se existe algum produto cadastrado, retornando True ou False'''
    
    planilha = "Produtos.xlsx"

    if not os.path.exists(planilha):
        print("Nenhum produto cadastrado.")
        return False
    
    df = pd.read_excel(planilha)

    if df.empty:
        print("Nenhum produto cadastrado na planilha")
        return False
    
    else:
        return True
    
def verificar_vendas():
    '''Função para verificar se existe algum produto vendido, retornando True ou False'''
    
    planilha = "Vendas.xlsx"

    if not os.path.exists(planilha):
        print("Nenhum produto vendido.")
        return False
    
    df = pd.read_excel(planilha)

    if df.empty:
        print("Nenhum produto vendido cadastrado na planilha")
        return False
    
    else:
        return True
    