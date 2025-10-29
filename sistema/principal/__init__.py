# importar o vendidoss
from sistema.venda import controle_de_vendas
from sistema.Cadastro import menu_crud
from sistema.uteis import *
from sistema.uteis.titulo import *
from sistema.Relatorio import menu_relatorio
from time import sleep

def principal(produto, vendidos):

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
            vendidos.append(controle_de_vendas(produto))
        elif opc == 3:
            if verificarLista(produto):
                subtitulo('>>> ESTOQUE <<<')
                print(f'\033[33mPRODUTO\033[m{" ":>28}\033[33mESTOQUE\033[m')
                for cad in produto:
                    print(f'{cad["estoque"]:<29}{cad["nome_do_produto"].upper():>13}')
                    print(linha())

        elif opc == 4:
            if verificarLista(vendidos, ' ERRO! NENHUMA VENDA! '):
                menu_relatorio(vendidos)
        elif opc == 5:
            if verificarLista(produto):
                subtitulo('>>> PRODUTOS CADASTRADOS <<<')
                for p in produto:
                    for k, v in p.items():
                        print(f'{k}: {v}')
                    print('=' * 42)
            print(linha())
        elif opc == 6:
            print('Você FECHOU O PROGRAMA... ')
            break


def menu(lista):
    cont = 1
    for op in lista:
        print(f'\033[32m{cont})\033[m \033[34m{op}\033[m')
        cont += 1
    print(linha())
    opc = leiaInt(f'Selecione a sua opção: ')
    sleep(0.5)
    return opc




