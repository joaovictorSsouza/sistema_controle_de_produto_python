from random import randint
from sistema.uteis.titulo import *
from sistema.uteis import *
from sistema.principal import *
from time import sleep



def cadastro_produto():
    '''
    Função que cadastra um produto.

    Recebe nome, preço e quantidade.

    Salvando todos os dados em um dicionário {produto}.

    :return: dict: Produto cadastrado
    '''
    produto = dict()

    produto['nome_do_produto'] = input('Nome do Produto:')
    produto['codigo_do_produto'] = randint(1000, 3000)
    produto['preco_produto'] = leiaFloat('Valor do Produto (Uni): R$')
    produto['estoque'] = leiaInt('No Estoque: ')
    produto['preco_compra'] = leiaFloat('Valor de comprar: R$')
    return produto


def menu_crud(produto):
    while True:
        subtitulo('>>> CADASTRO / EXCLUIR / ALTERAR <<<')
        print('''
        \033[32mA)\033[m \033[34mCADASTRO DO PRODUTO\033[m
        \033[32mB)\033[m \033[34mEXCLUIR PRODUTO\033[m
        \033[32mC)\033[m \033[34mALTERAR PRODUTO\033[m
        \033[32mD)\033[m \033[34mSAIR\033[m
        ''')
        escolha = validacaoOpc('O que gostaria de fazer? ')
        sleep(0.5)

        if escolha == 'A':
            subtitulo('>>> CADASTRO DO PRODUTO <<<')
            produto.append(cadastro_produto())
            print(f'Você salvou {produto[0]["nome_do_produto"].upper()} no programa com SUCESSO!')


        elif escolha == 'B':
            try:
                a = produto[0]
            except IndexError:
                print('\033[31mERRO! NÃO A NENHUM PRODUTO CADASTRADO\033[m')
            else:
                subtitulo('>>> EXCLUIR PRODUTO <<<')
                excluir_produto = input('Produto que gostaria de excluir, digite o nome: ')
                for p in produto:  # Acesso ao dicionario produtos
                    if p['nome_do_produto'] == excluir_produto:
                        produto.remove(p)
                        break
        elif escolha == 'C':
            if verificarLista(produto):
                subtitulo('>>> ALTERAÇÃO DE PRODUTO <<<')
                nome_alteracao = leiaOpc('Deseja alterar qual produto? ', produto)
                if nome_alteracao:
                    while True:
                        print(f'''
                        ALTERAR >>>
                        \033[32mA)\033[m \033[34mVALOR DO PRODUTO\033[m
                        \033[32mB)\033[m \033[34mVALOR DE COMPRA\033[m 
                        \033[32mC)\033[m \033[34mQUANTIDADE EM ESTOQUE\033[m
                        \033[32mD)\033[m \033[34mSAIR\033[m
                        ''')
                        alterar = input('Deseja alterar: ').upper()
                        sleep(0.5)
                        for p in produto:  # Acesso ao dicionario cadastrados
                            if p["nome_do_produto"] == nome_alteracao:
                                if alterar == 'A':
                                    novo_valor = leiaFloat('Novo valor: R$')
                                    p['preco_produto'] = novo_valor
                                    print('Novo valor cadastrado!')
                                elif alterar == 'B':
                                    novo_valor_compra = leiaFloat('Novo valor: R$')
                                    p['preco_compra'] = novo_valor_compra
                                    print('Novo valor de compra cadastrado!')
                                elif alterar == 'C':
                                    att_estoque = leiaFloat('Novo valor: R$')
                                    p['estoque'] = att_estoque
                                    print('Novo Estoque cadastrado!')
                                break
                        if alterar == 'D':
                            break
        elif escolha == 'D':
            break
