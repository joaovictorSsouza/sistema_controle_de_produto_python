def linha(tam=42):
    return '-' * tam

def titulos(msg):
    print("=" * 42)
    print(msg.center(42))
    print("=" * 42)

def subtitulo(msg):
    print()
    print(linha())
    print(f'{msg:^42}')
    print(linha())

def mensagem(msg):
    print(f'{msg:^42}')
    print("-=" * 24)
    