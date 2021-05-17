from src.dao.DAO import DAO
from src.db import db
from src.dao.DAOProduto import ProdutoDAO
from src.dao.DAOPagamento import PagamentoDAO
from src.dao.DAOCliente import ClienteDAO
from src.sys.venda import Venda, Carrinho

class CarrinhoDAO(DAO):

    def __parseDataToObject(self, data):
        data = list(data)

        listaProdutos = db.records(f'SELECT IDProduto, Quantidade FROM Carrinho_Produtos WHERE IDCarrinho = \'{data[0]}\'')
        preco = 0.0
        for i in range(len(listaProdutos)):
            produto = self.__ProdutoDAO.getByID(listaProdutos[i][0])
            listaProdutos[i] = list(listaProdutos[i])
            listaProdutos[i][0] = produto
            preco += (produto.read()[4]) * listaProdutos[i][1]
        


        return Carrinho(
            codigo= data[0],
            lista = listaProdutos,
            preco = preco
        )

    def __parsedList(self, Carrinho):
        lista = list(Carrinho.read())
        lista.pop(2)

        listaProdutos = lista.pop(1)

        for i in range(len(listaProdutos)):
            listaProdutos[i][0] = listaProdutos[i][0].read()[0]
        
        lista.append(listaProdutos)

        
        return lista

    def __init__(self, ProdutoDAO):
        super().__init__('CarrinhoDeProdutos', 'IDCarrinho')
        self.__ProdutoDAO = ProdutoDAO
    
    def add(self, Carrinho):
        lista  = self.__parsedList(Carrinho)
        db.execute(f'INSERT INTO CarrinhoDeProdutos VALUES (\'{lista[0]}\')')

        for produto in lista[1]:
            db.execute(f'INSERT INTO Carrinho_Produtos VALUES (\'{lista[0]}\', \'{produto[0]}\', \'{produto[1]}\')')

        db.commit()

    def getAll(self):
        carrinhos = super().getAll()
        parsedCarrinho = []
        for carrinho in carrinhos:
            parsedCarrinho.append(self.__parseDataToObject(carrinho))
        return parsedCarrinho

    def getByID(self, ID):
        carrinhos = self.select('*', f'IDCarrinho like \'%{ID}%\'')
        parsedCarrinho = []
        for carrinho in carrinhos:
            parsedCarrinho.append(self.__parseDataToObject(carrinho))
        return parsedCarrinho

class VendaDAO(DAO):

    def __parseDataToObject(self, data): ###########
        data = list(data)

        cliente = self.__ClienteDAO.getByID(data[1])
        carrinho = self.__CarrinhoDAO.getByID(data[3])[0]
        pagamento = self.__PagamentoDAO.getByType(data[4])
        
        data[1] = cliente
        data[3] = carrinho
        data[4] = pagamento


        return Venda(
            codigo= data[0],
            cliente= data[1],
            data= data[2],
            carrinho= data[3],
            pagamento= data[4],
            preco = data[5]
        )

    def __parsedList(self, Venda):
        lista = list(Venda.read())
        
        clienteID = lista[1].read()[0]
        pagamentoID = lista[4].read()[0]
        carrinhoID = lista[3].read()[0]

        carrinho = lista[3]

        lista[1] = clienteID
        lista[4] = pagamentoID
        lista[3] = carrinhoID

        lista2 = [lista, carrinho]

        
        return lista2

    def __init__(self, CarrinhoDAO, PagamentoDAO, ClienteDAO):
        super().__init__('Venda', 'IDVenda')
        self.__CarrinhoDAO = CarrinhoDAO
        self.__PagamentoDAO = PagamentoDAO
        self.__ClienteDAO = ClienteDAO
    
    def add(self, Venda):
        lista  = self.__parsedList(Venda)
        db.execute(f'INSERT INTO Venda VALUES (?,?,?,?,?,?)',list(lista[0]))

        self.__CarrinhoDAO.add(lista[1])

        db.commit()

    def getAll(self):
        vendas = super().getAll()
        parsedVenda = []
        for venda in vendas:
            parsedVenda.append(self.__parseDataToObject(venda))
        return parsedVenda

    def getByID(self, ID):
        vendas = self.select('*', f'IDVenda like \'%{ID}%\'')
        parsedVenda = []
        for venda in vendas:
            parsedVenda.append(self.__parseDataToObject(venda))
        return parsedVenda