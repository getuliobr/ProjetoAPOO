from uuid import uuid4

class CategoriaDeProduto:

    def __init__(self, nome, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.codigo = codigo
        self.nome = nome

    def update(self, nome= False):
        if(nome):
            self.nome = nome
    
    def read(self):
        return (self.codigo, self.nome)

class Produto:

    def __init__(self, descricao, fabricante, categoria, preco, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.codigo = codigo
        self.descricao = descricao
        self.fabricante = fabricante
        self.categoria = categoria
        self.preco = preco
    
    def update(self, descricao= False, fabricante= False, categoria= False, preco= False):
        if(descricao):
            self.descricao = descricao
        if(fabricante):
            self.fabricante = fabricante
        if(categoria):
            self.categoria = categoria
        if(preco):
            self.preco = preco
    
    def read(self):
        return (self.codigo, self.descricao, self.fabricante, self.categoria, self.preco)

    