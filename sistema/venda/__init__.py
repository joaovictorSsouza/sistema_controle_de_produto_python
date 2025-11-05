from time import sleep
from sistema.uteis import *
from sistema.Excel import * 
from sistema.uteis.titulo import *
from time import sleep

def controle_de_vendas(lista):
    '''Função para controle de vendas com condições para permitir
    somente se o produto digitado, estiver na planilha de produtos.'''

    venda = dict()
    planilha_produto = "Produtos.xlsx"
    df_produtos = pd.read_excel(planilha_produto)

    venda["produto_vendido"] = input('Nome do Produto vendido: ')
    #.isin() cria uma comparação booleana
    #.any() verifica se existe algum True.
    if df_produtos["nome_do_produto"].isin([venda["produto_vendido"]]).any():
        venda["quantidade_vendida"] = int(input('Quantidade de produto vendido: '))
        df_produtos.loc[df_produtos["nome_do_produto"] == venda["produto_vendido"], "estoque"] -= venda["quantidade_vendida"]
        df_produtos.to_excel("Produtos.xlsx", index=False)
        df_produtos.loc[df_produtos["nome_do_produto"] == venda["produto_vendido"], "preco_produto"] *= venda["quantidade_vendida"]
        df_produtos.to_excel("Produtos.xlsx", index=False)
        lista.append(venda)
        salvar_excel(lista, "Vendas.xlsx")
    else:
        print("\033[31mProduto não encontrado.\033[m")
        

        

        

        

        
    
    

