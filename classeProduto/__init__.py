class Produto:
    def __init__(self, nome_do_produto, codigo_do_produto, preco_produto, estoque, preco_compra, data):
        '''Função construtor da classe Produto.
        Args: nome do produto, codigo, preço, estoque e preço de compra.'''
        self.nome_do_produto = nome_do_produto
        self.codigo_do_produto = codigo_do_produto
        self.preco_produto = preco_produto
        self.estoque = estoque
        self.preco_compra = preco_compra    
        self.data = data


    def to_dict(self):
        '''Função para retornar um dicionário com os dados do produto.'''
        dadosProduto =  {"nome_do_produto": self.nome_do_produto,
                "codigo_do_produto": self.codigo_do_produto,
                "preco_produto": self.preco_produto,
                "estoque": self.estoque,
                "preco_compra": self.preco_compra,
                "data": self.data.strftime('%d/%m/%Y')}
        
        return dadosProduto
    
