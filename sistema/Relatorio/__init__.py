from sistema.uteis.titulo import *
from sistema.uteis import *
from time import sleep


def menu_relatorio(vendidos):
    while True:
        subtitulo('>>> RELATORIO <<<')
        print('''
            \033[32mA)\033[m \033[34mTOTAL VENDIDO\033[m
            \033[32mB)\033[m \033[34mPRODUTOS MAIS VENDIDOS\033[m
            \033[32mC)\033[m \033[34mSAIR\033[m
        ''')

        op_relatorio = validacaoOpc('Qual relatorio? ')
        sleep(0.5)
        if op_relatorio == 'A':
            totvendido = 0
            subtitulo('>>> TOTAL VENDIDO <<<')
            for v in vendidos:
                print(f'PRODUTO: {v["produto_vendido"]} QUANTIDADE VENDIDOS: {v["quantidade_vendida"]} ')
                totvendido += v["quantidade_vendida"]
            print(f'Quantidade vendida: {totvendido}')
        elif op_relatorio == 'B':
            subtitulo('>>> PRODUTOS MAIS VENDIDOS <<<')
            vendas_ordenadas = sorted(vendidos, key=lambda v: v["quantidade_vendida"], reverse=True)
            for i, v in enumerate(vendas_ordenadas):
                print(f'{i}ª: {v["produto_vendido"].upper()} >>> {v["quantidade_vendida"]} ')
        elif op_relatorio == 'C':
            break
