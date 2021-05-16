from src.dao.DAO import DAO
from src.db import db
from src.sys.cliente import Cliente, Animal, Raca, Especie

class ClienteDAO(DAO):

    def __init__(self):

        super().__init__('Cliente', 'Codigo')
    
    def add(self, Cliente):
        lista  = Cliente.read()
        db.execute(f'INSERT INTO Cliente VALUES (?,?,?,?,?,?,?,?)', lista)
        db.commit()
    
    def update(self, Cliente):
        lista = Cliente.read()

        db.execute(f'UPDATE Cliente SET Nome = {lista[1]}, Endereco = {lista[2]}, Cidade = {lista[3]}, Estado = {lista[4]}, Telefone = {lista[5]}, Documento = {lista[6]}, email = {lista[7]} WHERE Codigo = {lista[0]}')
        db.commit()
    
class RacaDAO(DAO):

    def __init__(self):

        super().__init__('Raca', 'Codigo')
    
    def add(self, Raca):
        lista = Raca.read()

        db.execute(f'INSERT INTO Raca VALUES (?,?)', lista)
        db.commit()
    
    def update(self, Raca):
        lista = Raca.read()

        db.execute(f'UPDATE Raca SET Descricao = {lista[1]} WHERE Codigo = {lista[0]}')
        db.commit()

class EspecieDAO(DAO):

    def __init__(self):

        super().__init__('Especie', 'Codigo')
    
    def add(self, Especie):
        lista = Especie.read()

        db.execute(f'INSERT INTO Especie VALUES (?,?)', lista)
        db.commit()
    
    def update(self, Especie):
        lista = Especie.read()

        db.execute(f'UPDATE Especie SET Nome = {lista[1]} WHERE Codigo = {lista[0]}')