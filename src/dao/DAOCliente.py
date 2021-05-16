from src.dao.DAO import DAO
from src.db import db
from src.sys.cliente import Cliente

class ClienteDAO(DAO):

    def __init__(self):

        super().__init__('Cliente', 'Codigo')
    
    def add(self, Cliente):
        lista  = Cliente.read()
        db.execute(f'INSERT INTO Cliente VALUES (?,?,?,?,?,?,?,?)', lista)
        db.commit()
    
    def update(self, Cliente):
        lista = Cliente.read()

        db.execute(f'UPDATE Cliente SET Nome = {lista[1]}, Endereco = {lista[2]}, Cidade = {lista[3]}, Estado = {lista[4]}, Telefone = {lista[5]}, Documento = {lista[6]}, email = {lista[7]}')
        db.commit()
    

