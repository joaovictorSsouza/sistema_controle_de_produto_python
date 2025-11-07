import pandas as pd
import os

def salvar_excel(lista_dados, nome_arquivo):
    """ Função para salvar excel""" 

    if not lista_dados:
        print("Nenhum dado para salvar")
        return
    
    df = pd.DataFrame(lista_dados)

    if os.path.exists(nome_arquivo):
        df_existente = pd.read_excel(nome_arquivo)
        df = pd.concat([df_existente, df], ignore_index=True)

    df.to_excel(nome_arquivo, index=False)
    print(f"Dados salvos em {nome_arquivo} com sucesso!")

def relatorio_vendas():
    '''Função para gerar relatório de vendas baseada na planilha de vendas'''

    arquivo = "Vendas.xlsx"

    if not os.path.exists(arquivo):
        print("Nenhuma venda registrada")
        return 
    
    df = pd.read_excel(arquivo)
    print(df)

def estoque():
    '''Função para gerar relatório de estoque a partir da planilha de produtos'''


    arquivo = "Produtos.xlsx"

    if not os.path.exists(arquivo):
        print("Nenhum produto registrado.")
        return
    
    df = pd.read_excel(arquivo)
    print(df[["nome_do_produto", "estoque"]])


def cadastrados():
    '''Função para verificar a existencia de um produto cadastrado'''

    planilha = "Produtos.xlsx"

    if not os.path.exists(planilha):
        ("Nenhum cadastrado")
        return

    df = pd.read_excel(planilha)
    print(df)
        


    