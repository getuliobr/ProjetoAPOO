from src.sys.cliente import Cliente
from src.dao.DAOCliente import ClienteDAO

a = ClienteDAO()
b = Cliente(1, 'teste', 'rua de teste', 'cidade teste', 'teste', 22033445566, 23456789101, 'email@teste.com')

a.add(b)