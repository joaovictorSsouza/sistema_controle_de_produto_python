from random import randint
from classeProduto import *
import pandas as pd 
from sistema.uteis.titulo import *
from sistema.uteis import *
from sistema.principal import *
from sistema.Excel import *
from time import sleep



def cadastro_produto():
    '''
    Função que cadastra um produto.

    Recebe nome, preço e quantidade.

    Salvando todos os dados em um dicionário {produto}.

    :return: dict: Produto cadastrado
    '''
    produto = dict()

    nome = input('Nome do Produto:')
    codigo = randint(1000, 3000)
    preco_produto = leiaFloat('Valor do Produto (Uni): R$')
    estoque = leiaInt('No Estoque: ')
    preco_compra = leiaFloat('Valor de comprar: R$')

    #passando como arg os atributos para conta
    return Produto(nome, codigo, preco_produto, estoque, preco_compra)




def menu_crud(produto):
    '''Função que guia o menu CRUD dentro do cadastro
       Args: Recebe uma lista - Produtos'''
    

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
            novo_produto = cadastro_produto()
            dic_produto = novo_produto.to_dict()
            produto.append(dic_produto)
            sleep(0.5)
            salvar_excel(produto, "Produtos.xlsx")
            produto.clear()
            
        elif escolha == 'B':

            df = pd.read_excel("Produtos.xlsx")


            if df.empty:
                print("\033[31mNENHUM PRODUTO CADASTRADO\033[m")
            else:
                 subtitulo('>>> EXCLUIR PRODUTO <<<')
                 excluir_produto = input('Produto que gostaria de excluir, digite o nome: ')
                 if df["nome_do_produto"].isin([excluir_produto]).any():
                     mascara = df["nome_do_produto"] == excluir_produto # Mascara para acessar exatamente a linha da planilha que desejo
                     df.drop(df[mascara].index, inplace=True) # .drop() seerve para apagar dentro de pandas
                     df.to_excel("Produtos.xlsx", index=False) #index=false reoorganiza os index da planilha 
            break

        elif escolha == 'C':
            
            df = pd.read_excel("Produtos.xlsx")
            if df.empty:
                print("\033[31mNENHUM PRODUTO CADASTRADO\033")
                
            else:
                subtitulo('>>> ALTERAR PRODUTO <<<')
                nome_alteracao = input('Produto que gostaria de alterar, digite o nome: ')
                if df["nome_do_produto"].isin([nome_alteracao]).any():
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
                        if alterar == 'A':
                            novo_valor = leiaFloat('Novo valor: R$')
                            df.loc[df["nome_do_produto"] == nome_alteracao, "preco_produto"] = novo_valor
                            df.to_excel("Produtos.xlsx", index=False)
                            print('Novo valor cadastrado!')
                            break
                        
                        elif alterar == 'B':
                            novo_valor_compra = leiaFloat('Novo valor: R$')
                            df.loc[df["nome_do_produto"] == nome_alteracao, "preco_compra"] = novo_valor_compra
                            df.to_excel("Produtos.xlsx", index=False)
                            print('Novo valor de compra cadastrado!')
                            break
                        
                        elif alterar == 'C':
                            att_estoque = leiaFloat('Novo valor: R$')
                            df.loc[df["nome_do_produto"] == nome_alteracao, "estoque"] = att_estoque
                            df.to_excel("Produtos.xlsx", index=False)
                            print('Novo Estoque cadastrado!')
                            break
                        
                        if alterar == 'D':
                            break
        elif escolha == 'D':
            break
