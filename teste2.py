from src.dao.DAOCliente import ClienteDAO
from src.dao.DAOPagamento import PagamentoDAO
from src.sys.cliente import Cliente
from src.sys.venda import Venda
from src.sys.pagamento import Pagamento
from src.sys.produto import CategoriaDeProduto, Produto
from src.dao.DAOVenda import CarrinhoDAO, Carrinho, VendaDAO
from src.dao.DAOProduto import ProdutoDAO,CategoriaDeProdutoDAO


CategoriaDeProdutoDAO = CategoriaDeProdutoDAO()
ProdutoDAO = ProdutoDAO(CategoriaDeProdutoDAO)
PagamentoDAO = PagamentoDAO()

categoria1 = CategoriaDeProduto('sisisisiis')
produto1 = Produto('19836289','sim', categoria1, 15.5)
produto2 = Produto('15165','verdade', categoria1, 10)

CategoriaDeProdutoDAO.add(categoria1)
ProdutoDAO.add(produto1)
ProdutoDAO.add(produto2)


pagamento1 = Pagamento('ablkulu')


ClienteDAO = ClienteDAO()

cliente1 = Cliente('ooaoao', '1sau', 's9ausa', '09723jio', 54154161, 1556155441, 'dsiaodha')

ClienteDAO.add(cliente1)

venda1 = Venda(cliente1)
print(venda1.read())
venda1.addProduto(produto1)
venda1.addProduto(produto1)
print(venda1.read()[3].read())
venda1.removeProduto(produto1)
venda1.addPagamento(pagamento1)
print(venda1.read())

CarrinhoDAO = CarrinhoDAO(ProdutoDAO)

# carrinho1 = Carrinho()
# carrinho1.addProduto(produto1)
# carrinho1.addProduto(produto1)
# carrinho1.addProduto(produto2)

# CarrinhoDAO.add(carrinho1)

VendaDAO = VendaDAO(CarrinhoDAO, PagamentoDAO, ClienteDAO)

VendaDAO.add(venda1)

print(VendaDAO.getByID(venda1.read()[0])[0].read())

