from uuid import uuid4
from datetime import datetime

from src.sys.pagamento import Pagamento

class Carrinho:

    def __init__(self, codigo = None, lista = None, preco = None):
        if not codigo:
            codigo = str(uuid4())
        if not lista:
            lista = []
        if not preco:
            preco = 0.0

        self.__codigo = codigo
        self.__lista = lista
        self.__preco = preco

    def __haveProduto(self,produto):
        for i in range(len(self.__lista)):
            if (self.__lista[i][0].read())[0] == produto.read()[0]:
                return i
        return -1

    def addProduto(self, produto):
        temProduto = self.__haveProduto(produto)
        if temProduto > -1:
            self.__lista[temProduto][1] += 1
            self.__preco += produto.read()[4]
        else:
            self.__lista.append([produto, 1])
            self.__preco += produto.read()[4]
    
    def removeProduto(self, produto):
        temProduto = self.__haveProduto(produto)
        if temProduto > -1:
            if(self.__lista[temProduto][1] > 1):
                self.__lista[temProduto][1] -= 1
            else:
                self.__lista.pop(temProduto)
            self.__preco -= produto.read()[4]
    

    def read(self):
        return (self.__codigo, self.__lista, self.__preco)

class Venda:

    def __init__(self, cliente, codigo= None, data = None, carrinho = None, pagamento = None,preco = None):
        if not codigo:
            codigo = str(uuid4())
        if not data:
            data = '11/09/2001'
        if not carrinho:
            carrinho = Carrinho()
        if not preco:
            preco = 0.0
        self.__codigo = codigo
        self.__cliente = cliente
        self.__data = data
        self.__carrinho = carrinho
        self.__preco = preco
        self.__formadePagamento =  pagamento

    def addProduto(self, Produto):
        self.__carrinho.addProduto(Produto)
        self.__preco = self.carrinho.read()[2]


    def removeProduto(self, Produto):
        self.__carrinho.removeProduto(Produto)
        self.__preco = self.carrinho.read()[2]
    
    def addPagamento(self, pagamento):
        self.__formadePagamento = pagamento

    def read(self):
        return(self.__codigo, self.__cliente, self.__data, self.__carrinho, self.__formadePagamento, self.__preco)







    


