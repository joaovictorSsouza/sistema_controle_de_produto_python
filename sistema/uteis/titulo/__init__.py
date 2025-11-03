def linha(tam=42):
    '''Função para geral uma linha de tamanho definido em 42 caracteres.'''
    return '-' * tam

def titulos(msg):
    '''Função para chamar um titulo com linha e mensagem.
    param: Mensagem que gostaria de mostrar.'''

    print("=" * 42)
    print(msg.center(42))
    print("=" * 42)

def subtitulo(msg):
    '''Função para chamar e criar um subtitulo para o terminal.
    param: Mensagem que gostaria de mostrar.'''
    print()
    print(linha())
    print(f'{msg:^42}')
    print(linha())

def mensagem(msg):
    '''Função para chamar e criar uma mensagem para o terminal.
    param: Mensagem que gostaria de mostrar.'''
    
    print(f'{msg:^42}')
    print("-=" * 24)
    