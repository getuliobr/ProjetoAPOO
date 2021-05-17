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

        self.codigo = codigo
        self.lista = lista
        self.preco = preco

    def __haveProduto(self,produto):
        for i in range(len(self.lista)):
            if (self.lista[i][0].read())[0] == produto.read()[0]:
                return i
        return -1

    def addProduto(self, produto):
        temProduto = self.__haveProduto(produto)
        if temProduto > -1:
            self.lista[temProduto][1] += 1
            self.preco += produto.read()[4]
        else:
            self.lista.append([produto, 1])
            self.preco += produto.read()[4]
    
    def removeProduto(self, produto):
        temProduto = self.__haveProduto(produto)
        if temProduto > -1:
            if(self.lista[temProduto][1] > 1):
                self.lista[temProduto][1] -= 1
            else:
                self.lista.pop(temProduto)
            self.preco -= produto.read()[4]
    

    def read(self):
        return (self.codigo, self.lista, self.preco)

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
        self.codigo = codigo
        self.cliente = cliente
        self.data = data
        self.carrinho = carrinho
        self.preco = preco
        self.formadePagamento =  pagamento

    def addProduto(self, Produto):
        self.carrinho.addProduto(Produto)
        self.preco = self.carrinho.read()[2]


    def removeProduto(self, Produto):
        self.carrinho.removeProduto(Produto)
        self.preco = self.carrinho.read()[2]
    
    def addPagamento(self, pagamento):
        print(self.formadePagamento, pagamento)
        self.formadePagamento = pagamento

    def read(self):
        return(self.codigo, self.cliente, self.data, self.carrinho, self.formadePagamento, self.preco)







    


