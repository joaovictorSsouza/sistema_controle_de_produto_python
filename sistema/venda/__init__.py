from sistema.uteis import *
from sistema.Excel import * 
from sistema.uteis.titulo import *
from datetime import datetime

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
        # Atualiza o estoque no DataFrame de produtos e salva no Excel
        df_produtos.loc[df_produtos["nome_do_produto"] == venda["produto_vendido"], "estoque"] -= venda["quantidade_vendida"]
        df_produtos.to_excel("Produtos.xlsx", index=False)
        # Calcula o preço total da venda e adiciona ao dicionário da venda
        preco_unitario = df_produtos.loc[df_produtos["nome_do_produto"] == venda["produto_vendido"], "preco_produto"].iloc[0]
        venda["preco_venda"] = preco_unitario * venda["quantidade_vendida"]
        while True:
            data_str = input("Data da venda (dd/mm/aaaa): ")
            try:
                data = datetime.strptime(data_str, '%d/%m/%Y').date()
                venda["Data_venda"] = data.strftime('%d/%m/%Y')
                break
            except ValueError:
                print("\033[31mFormato de data inválido! Por favor, use o formato dd/mm/aaaa.\033[m")
        lista.append(venda)
        salvar_excel(lista, "Vendas.xlsx")
    else:
        print("\033[31mProduto não encontrado.\033[m")
        

        

        

        

        
    
    
