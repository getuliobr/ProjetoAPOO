
class CategoriaDeProduto:

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def update(self, codigo= False, nome= False):
        if(codigo):
            self.codigo = codigo
        if(nome):
            self.nome = nome
    
    def read(self):
        return (self.codigo, self.nome)

class Produto:

    def __init__(self, codigo, descricao, fabricante, categoria, preco):
        self.codigo = codigo
        self.descricao = descricao
        self.fabricante = fabricante
        self.categoria = categoria
        self.preco = preco
    
    def update(self, codigo= False, descricao= False, fabricante= False, categoria= False, preco= False):
        if(codigo):
            self.codigo = codigo
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

    