from src.dao.DAO import DAO
from src.db import db
from src.sys.classes import Veterinario, Atendente, Administrador

class VeterinarioDAO(DAO):

    def __parseDataToObject(self, data):
        return Veterinario(
            codigo= data[0],
            nome= data[1],
            endereco= data[2],
            cidade= data[3],
            estado= data[4],
            foneResidencia= data[5],
            foneCelular= data[6]
        )

    def __init__(self):
        super().__init__('Veterinario', 'Codigo')

    def add(self, Veterinario):
        lista  = Veterinario.read()
        t = db.execute(f'INSERT INTO Veterinario VALUES (?,?,?,?,?,?,?)', lista)
        db.commit()
        return t

    def update(self, Veterinario):
        lista = Veterinario.read()

        db.execute(f'UPDATE Veterinario SET Nome = \'{lista[1]}\', Endereco = \'{lista[2]}\', Cidade = \'{lista[3]}\', Estado = \'{lista[4]}\', Telefone = \'{lista[5]}\', Documento = \'{lista[6]}\', email = \'{lista[7]}\' WHERE Codigo = \'{lista[0]}\'')
        db.commit()

    def getByID(self, ID):
        veterinario = super().getByID(ID)
        if not veterinario:
            return None
        return self.__parseDataToObject(veterinario)

    def getAll(self):
        veterinarios = super().getAll()
        parsedVeterinario = []
        for veterinario in veterinarios:
            parsedVeterinario.append(self.__parseDataToObject(veterinario))
        return parsedVeterinario

    def getByName(self, nome):
        veterinarios = self.select('*', f'Nome like \'%{nome}%\'')
        parsedVeterinario = []
        for veterinario in veterinarios:
            parsedVeterinario.append(self.__parseDataToObject(veterinario))
        return parsedVeterinario

class AtendenteDAO(DAO):

    def __parseDataToObject(self, data):
        return Atendente(
            codigo= data[0],
            nome= data[1]
        )

    def __init__(self):
        super().__init__('Atendente', 'Codigo')

    def add(self, Atendente):
        lista  = Atendente.read()
        t = db.execute(f'INSERT INTO Atendente VALUES (?,?)', lista)
        db.commit()
        return t

    def update(self, Atendente):
        lista = Atendente.read()

        db.execute(f'UPDATE Atendente SET Nome = \'{lista[1]}\' WHERE Codigo = \'{lista[0]}\'')
        db.commit()

    def getByID(self, ID):
        atendente = super().getByID(ID)
        if not atendente:
            return None
        return self.__parseDataToObject(atendente)

    def getAll(self):
        atendentes = super().getAll()
        parsedAtendente = []
        for atendente in atendentes:
            parsedAtendente.append(self.__parseDataToObject(atendente))
        return parsedAtendente

    def getByName(self, nome):
        atendentes = self.select('*', f'Nome like \'%{nome}%\'')
        parsedAtendente = []
        for atendente in atendentes:
            parsedAtendente.append(self.__parseDataToObject(atendente))
        return parsedAtendente

class AdministradorDAO(DAO):

    def __parseDataToObject(self, data):
        return Administrador(
            codigo= data[0],
            nome= data[1]
        )

    def __init__(self):
        super().__init__('Administrador', 'Codigo')

    def add(self, Administrador):
        lista  = Administrador.read()
        t = db.execute(f'INSERT INTO Administrador VALUES (?,?)', lista)
        db.commit()
        return t

    def update(self, Administrador):
        lista = Administrador.read()

        db.execute(f'UPDATE Administrador SET Nome = {lista[1]} WHERE Codigo = {lista[0]}')
        db.commit()

    def getByID(self, ID):
        administrador = super().getByID(ID)
        if not administrador:
            return None
        return self.__parseDataToObject(administrador)

    def getAll(self):
        administradores = super().getAll()
        parsedAdministrador = []
        for administrador in administradores:
            parsedAdministrador.append(self.__parseDataToObject(administrador))
        return parsedAdministrador

    def getByName(self, nome):
        administradores = self.select('*', f'Nome like \'%{nome}%\'')
        parsedAdministrador = []
        for administrador in administradores:
            parsedAdministrador.append(self.__parseDataToObject(administrador))
        return parsedAdministrador