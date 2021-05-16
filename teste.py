from src.sys.cliente import Cliente
from src.dao.DAOCliente import ClienteDAO

a = ClienteDAO()
b = Cliente('teste', 'rua de teste', 'cidade teste', 'teste', 22033445566, 23456789101, 'email@teste.com')

id = b.read()[0]

print(a.add(b))
print(a.getByID(str('19c82b6f-cb0a-4aa2-ab6a-39d5a6b39106')))
