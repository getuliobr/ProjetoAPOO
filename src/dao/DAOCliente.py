from src.dao.DAO import DAO
from src.db import db
from src.sys.cliente import Cliente, Animal, Raca, Especie

class ClienteDAO(DAO):

    def __parseDataToObject(self, data):
        return Cliente(
            codigo= data[0],
            nome= data[1],
            endereco= data[2],
            cidade= data[3],
            estado= data[4],
            telefone= data[5],
            documento= data[6],
            email= data[7]
        )

    def __init__(self):
        super().__init__('Cliente', 'Codigo')

    def add(self, Cliente):
        lista  = Cliente.read()
        t = db.execute(f'INSERT INTO Cliente VALUES (?,?,?,?,?,?,?,?)', lista)
        db.commit()
        return t

    def update(self, Cliente):
        lista = Cliente.read()

        db.execute(f'UPDATE Cliente SET Nome = \'{lista[1]}\', Endereco = \'{lista[2]}\', Cidade = \'{lista[3]}\', Estado = \'{lista[4]}\', Telefone = \'{lista[5]}\', Documento = \'{lista[6]}\', email = \'{lista[7]}\' WHERE Codigo = \'{lista[0]}\'')
        db.commit()

    def getByID(self, ID):
        cliente = super().getByID(ID)
        if not cliente:
            return None
        return self.__parseDataToObject(cliente)

    def getAll(self):
        clientes = super().getAll()
        parsedCliente = []
        for cliente in clientes:
            parsedCliente.append(self.__parseDataToObject(cliente))
        return parsedCliente

    def getByName(self, nome):
        clientes = self.select('*', f'Nome like \'%{nome}%\'')
        parsedCliente = []
        for cliente in clientes:
            parsedCliente.append(self.__parseDataToObject(cliente))
        return parsedCliente
    
class RacaDAO(DAO):

    def __parseDataToObject(self, data):
        return Raca(
            codigo= data[0],
            descricao= data[1]
        )

    def __init__(self):
        super().__init__('Raca', 'Codigo')
    
    def add(self, Raca):
        lista  = Raca.read()
        t = db.execute(f'INSERT INTO Raca VALUES (?,?)', lista)
        db.commit()
        return t

    def update(self, Raca):
        lista = Raca.read()

        db.execute(f'UPDATE Raca SET Descricao = {lista[1]} WHERE Codigo = {lista[0]}')
        db.commit()

    def getByID(self, ID):
        raca = super().getByID(ID)
        if not raca:
            return None
        return self.__parseDataToObject(raca)

    def getAll(self):
        racas = super().getAll()
        parsedRaca = []
        for raca in racas:
            parsedRaca.append(self.__parseDataToObject(raca))
        return parsedRaca

    def getByDescricao(self, descricao):
        racas = self.select('*', f'Descricao like \'%{descricao}%\'')
        parsedRaca = []
        for raca in racas:
            parsedRaca.append(self.__parseDataToObject(raca))
        return parsedRaca

class EspecieDAO(DAO):

    def __parseDataToObject(self, data):
        return Especie(
            codigo= data[0],
            nome= data[1]
        )

    def __init__(self):
        super().__init__('Especie', 'Codigo')
    
    def add(self, Especie):
        lista  = Especie.read()
        t = db.execute(f'INSERT INTO Especie VALUES (?,?)', lista)
        db.commit()
        return t

    def update(self, Especie):
        lista = Especie.read()

        db.execute(f'UPDATE Especie SET Nome = {lista[1]} WHERE Codigo = {lista[0]}')
        db.commit()

    def getByID(self, ID):
        especie = super().getByID(ID)
        if not especie:
            return None
        return self.__parseDataToObject(especie)

    def getAll(self):
        especies = super().getAll()
        parsedEspecie = []
        for especie in especies:
            parsedEspecie.append(self.__parseDataToObject(especie))
        return parsedEspecie

    def getByName(self, Nome):
        especies = self.select('*', f'Nome like \'%{Nome}%\'')
        parsedEspecie = []
        for especie in especies:
            parsedEspecie.append(self.__parseDataToObject(especie))
        return parsedEspecie

class AnimalDAO(DAO):
    
    def __parseDataToObject(self, data):
        data = list(data)
        dono = self.__ClienteDAO.getByID(data[2])
        data[2] = dono
        especie = self.__EspecieDAO.getByID(data[4])
        data[4] = especie
        raca = self.__RacaDAO.getByID(data[5])
        data[5] = raca

        return Animal(
            codigo= data[0],
            nome= data[1],
            dono= data[2],
            dataNascimento= data[3],
            especie= data[4],
            raca= data[5],
            sexo = data[6],
            cor = data[7]
        )

    def __parsedList(self, Animal):
        lista = list(Animal.read())
        clienteID = (lista[2].read())[0]
        lista[2] = clienteID
        especieID = (lista[4].read())[0]
        lista[4] = especieID
        racaID = (lista[5].read())[0]
        lista[5] = racaID
        
        return tuple(lista)

    def __init__(self, ClienteDAO, EspecieDAO, RacaDAO):
        super().__init__('Animal', 'Codigo')
        self.__ClienteDAO = ClienteDAO
        self.__EspecieDAO = EspecieDAO
        self.__RacaDAO = RacaDAO
    
    def add(self, Animal):
        lista  = self.__parsedList(Animal)
        t = db.execute(f'INSERT INTO Animal VALUES (?,?,?,?,?,?,?,?)', lista)
        db.commit()
        return t

    def update(self, Animal):
        lista = self.__parsedList(Animal)

        db.execute(f'UPDATE Animal SET Nome = {lista[1]}, Dono = {lista[2]}, DataNascimento = {lista[3]}, Especie = {lista[4]}, Raca = {lista[5]}, Sexo = {lista[6]}, Cor = {lista[7]}  WHERE Codigo = {lista[0]}')
        db.commit()

    def getByID(self, ID):
        animal = super().getByID(ID)
        if not animal:
            return None
        return self.__parseDataToObject(animal)

    def getAll(self):
        animais = super().getAll()
        parsedAnimal = []
        for animal in animais:
            parsedAnimal.append(self.__parseDataToObject(animal))
        return parsedAnimal

    def getByName(self, Nome):
        animais = self.select('*', f'Nome like \'%{Nome}%\'')
        parsedAnimal = []
        for animal in animais:
            parsedAnimal.append(self.__parseDataToObject(animal))
        return parsedAnimal

    def getClientAnimals(self, Cliente):
        clienteID = Cliente.read()[0]
        animals = self.select('*', f'Dono = \'{clienteID}\'')
        animalsParsed = []
        for animal in animals:
            animalsParsed.append(self.__parseDataToObject(animal))
        return animalsParsed