from src.dao.DAO import DAO
from src.db import db
from src.sys.produto import Produto, CategoriaDeProduto

class CategoriaDeProdutoDAO(DAO):
    
    def __parseDataToObject(self, data):
        return CategoriaDeProduto(
            codigo= data[0],
            nome= data[1]
        )

    def __init__(self):
        super().__init__('CategoriaDeProduto', 'Codigo')
    
    def add(self, CategoriaDeProduto):
        lista  = CategoriaDeProduto.read()
        t = db.execute(f'INSERT INTO CategoriaDeProduto VALUES (?,?)', lista)
        db.commit()
        return t

    def update(self, CategoriaDeProduto):
        lista = CategoriaDeProduto.read()

        db.execute(f'UPDATE CategoriaDeProduto SET Nome = {lista[1]} WHERE Codigo = {lista[0]}')
        db.commit()

    def getByID(self, ID):
        categoria = super().getByID(ID)
        if not categoria:
            return None
        return self.__parseDataToObject(categoria)

    def getAll(self):
        categorias = super().getAll()
        parsedCategoria = []
        for categoria in categorias:
            parsedCategoria.append(self.__parseDataToObject(categoria))
        return parsedCategoria

    def getByName(self, Nome):
        categorias = self.select('*', f'Nome like \'%{Nome}%\'')
        parsedCategoria = []
        for categoria in categorias:
            parsedCategoria.append(self.__parseDataToObject(categoria))
        return parsedCategoria

class ProdutoDAO(DAO):

    def __parseDataToObject(self, data):
        categoria = CategoriaDeProdutoDAO.getByID(data[3])
        data[3] = categoria

        return Produto(
            codigo= data[0],
            descricao= data[1],
            fabricante= data[2],
            categoria= data[3],
            preco= data[4]
        )

    def __parsedList(self, Produto):
        lista = Produto.read()
        categoriaID = (lista[3].read())[0]
        lista[3] = categoriaID
        
        return lista

    def __init__(self):
        super().__init__('Produto', 'Codigo')
    
    def add(self, Produto):
        lista  = self.__parsedList(Produto)
        t = db.execute(f'INSERT INTO Produto VALUES (?,?,?,?,?)', lista)
        db.commit()
        return t

    def update(self, Produto):
        lista = self.__parsedList(Produto)

        db.execute(f'UPDATE Produto SET Descricao = {lista[1]}, Fabricante = {lista[2]}, Categoria = {lista[3]}, Preco = {lista[4]} WHERE Codigo = {lista[0]}')
        db.commit()

    def getByID(self, ID):
        produto = super().getByID(ID)
        if not produto:
            return None
        return self.__parseDataToObject(produto)

    def getAll(self):
        produtos = super().getAll()
        parsedProduto = []
        for produto in produtos:
            parsedProduto.append(self.__parseDataToObject(produto))
        return parsedProduto

    def getByType(self, Tipo, Nome): 
        produtos = self.select('*', f'{Tipo} like \'%{Nome}%\'')
        parsedProduto = []
        for produto in produtos:
            parsedProduto.append(self.__parseDataToObject(produto))
        return parsedProduto