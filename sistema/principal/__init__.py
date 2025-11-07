from sistema.venda import controle_de_vendas
from sistema.Cadastro import menu_crud
from sistema.Excel import *
from sistema.uteis import *
from sistema.uteis.titulo import *
from time import sleep


def principal(produto, vendidos):
    '''Função para chamar o menu principal do sistema
    param: Lista: Produto e vendidos'''


    planilha_vendas = "Vendas.xlsx"
    planilha_produto = "Produtos.xlsx"

    while True:
        subtitulo('>>> MENU <<<')
        opc = menu(['CADASTRO / EXCLUIR / ALTERAR',
              'CONTROLE DE VENDAS',
              'ESTOQUE',
              'RELATORIO',
              'PRODUTOS CADASTRADOS',
              'SAIR'])
        
        if opc == 1:
            menu_crud(produto)

        elif opc == 2:
            
            df = pd.read_excel(planilha_produto)
            if df.empty:
                print("\033[31mNENHUM PRODUTO CADASTRADO\033[m")
            else:
                controle_de_vendas(vendidos)
                
                     
        elif opc == 3:

            df = pd.read_excel(planilha_produto)
            if df.empty:
                print("\033[31mNENHUM PRODUTO CADASTRADO\033[m")
            else:
                subtitulo('>>> ESTOQUE <<<')
                estoque()
                print(linha())

        elif opc == 4:

            df = pd.read_excel(planilha_vendas)
            if df.empty:
                print("\033[31mNENHUMA VENDA REGISTRADA\033[m")
            else:    
                subtitulo('>>> RELATORIO DE VENDAS <<<')
                relatorio_vendas()

        elif opc == 5:

            df = pd.read_excel(planilha_produto)
            if df.empty:
                print("\033[31mNENHUM PRODUTO CADASTRADO\033[m")
            else:
                subtitulo('>>> PRODUTOS CADASTRADOS <<<')
                cadastrados()
                print(linha())

        elif opc == 6:
            print('Você FECHOU O PROGRAMA... ')
            break


def menu(lista):
    '''Função que cria um menu com opções'''
    cont = 1
    for op in lista:
        print(f'\033[32m{cont})\033[m \033[34m{op}\033[m')
        cont += 1
    print(linha())
    opc = leiaInt(f'Selecione a sua opção: ')
    sleep(0.5)
    return opc




