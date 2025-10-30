from time import sleep
from sistema.uteis import *
from sistema.uteis.titulo import *
from time import sleep

def controle_de_vendas(produto):
    venda = dict()
    if verificarLista(produto):
        venda["produto_vendido"] = input('Nome do Produto vendido: ')
        sleep(0.5)
        for cadastrado in produto:
            if venda["produto_vendido"] == cadastrado["nome_do_produto"]:
                    venda["quantidade_vendida"] = int(input('Quantidade de produto vendido: '))
                    #diminuir do estoque a quantidade de vendas.
                    for p in produto:
                        if venda["produto_vendido"] == p["nome_do_produto"]:
                            if p["estoque"] >= venda["quantidade_vendida"]:
                                p["estoque"] -= venda["quantidade_vendida"]
                                venda["data_da_venda"] = input('Data da Venda: [dd/mm/aaaa]')
                            else:
                                print()
                                print(f'!!!!! NÃO TEMOS ESTOQUE SUFICIENTE !!!!!')
            elif not any(venda["produto_vendido"] == cadastrado["nome_do_produto"] for cadastrado in produto):
                print('\033[31mPRODUTO NÃO CADASTRADO\033[m')
    return venda
