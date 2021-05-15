from . import produto
from datetime import datetime

class Carrinho:

    def adicionarProduto(self, produto):
        if(produto):
            self.lista.append(produto, 1) #Procurar se já existe o produto, se sim adicionar a quantidade
            self.preco += produto.preco
        else:
            self.lista.append(produto, 1)
            self.preco += produto.preco
    
    def removerProduto(self, produto):
        if(produto):
            remover = 1
    
    def verLista(self):
        return (self.lista, self.preco)

class Venda:

    def __init__(self, cliente):
        self.cliente = cliente
        self.data = datetime.now()
        self.carinho = Carrinho()

    def adicionarProduto(self):
        pass

    def removerProduto(self):
        pass
    
    def formadePagamento(self, pagamento):
        self.formadePagamento = pagamento






    


