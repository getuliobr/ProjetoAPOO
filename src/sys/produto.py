from uuid import uuid4

class CategoriaDeProduto:

    def __init__(self, nome, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.__codigo = codigo
        self.__nome = nome

    def update(self, nome= False):
        if(nome):
            self.__nome = nome
    
    def read(self):
        return (self.__codigo, self.__nome)

class Produto:

    def __init__(self, descricao, fabricante, categoria, preco, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.__codigo = codigo
        self.__descricao = descricao
        self.__fabricante = fabricante
        self.__categoria = categoria
        self.__preco = preco
    
    def update(self, descricao= False, fabricante= False, categoria= False, preco= False):
        if(descricao):
            self.__descricao = descricao
        if(fabricante):
            self.__fabricante = fabricante
        if(categoria):
            self.__categoria = categoria
        if(preco):
            self.__preco = preco
    
    def read(self):
        return (self.__codigo, self.__descricao, self.__fabricante, self.__categoria, self.__preco)

    