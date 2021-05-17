from src.dao.DAO import DAO
from src.db import db
from src.dao.DAOClasses import Veterinario, VeterinarioDAO
from src.dao.DAOCliente import Cliente, Animal, ClienteDAO, AnimalDAO
from src.dao.DAOPagamento import Pagamento, PagamentoDAO
from src.dao.DAOProduto import Produto, ProdutoDAO
from sys.consulta import Servico, Consulta

class ServicoDAO(DAO):

    def __parseDataToObject(self, data):
        return Servico(
            codigo= data[0],
            descricao= data[1],
            preco= data[2]
        )

    def __init__(self):
        super().__init__('Servico', 'Codigo')
    
    def add(self, Servico):
        lista  = Servico.read()
        t = db.execute(f'INSERT INTO Servico VALUES (?,?,?)', lista)
        db.commit()
        return t

    def update(self, Servico):
        lista = Servico.read()

        db.execute(f'UPDATE Servico SET Descricao = {lista[1]}, Preco = {lista[2]} WHERE Codigo = {lista[0]}')
        db.commit()

    def getByID(self, ID):
        servico = super().getByID(ID)
        if not servico:
            return None
        return self.__parseDataToObject(servico)

    def getAll(self):
        servicos = super().getAll()
        parsedServico = []
        for servico in servicos:
            parsedServico.append(self.__parseDataToObject(servico))
        return parsedServico

    def getByDescricao(self, Descricao):
        descricoes = self.select('*', f'Descricao like \'%{Descricao}%\'')
        parsedDescricao = []
        for descricao in descricoes:
            parsedDescricao.append(self.__parseDataToObject(descricao))
        return parsedDescricao

class ConsultaDAO(DAO):

    def __parseDataToObject(self, data): ##################
        data = list(data)
        cliente = self.__ClienteDAO.getByID(data[2])
        animal = self.__AnimalDAO.getByID(data[3])
        veterinario = self.__VeterinarioDAO.getByID(data[4])
        pagamento = self.__PagamentoDAO.getByID(data[5])
        servico = self.__ServicoDAO.getByID(data[6])
        data[2] = cliente
        data[3] = animal
        data[4] = veterinario
        data[5] = pagamento
        data[6] = servico

        medicamentos = list(db.records('SELECT IDProduto, Quantidade FROM Consulta_Medicamentos WHERE IDConsulta = ?',data[0]))


        return Consulta(
            codigo= data[0],
            data= data[1],
            dono= data[2],
            animal= data[3],
            veterinario= data[4],
            pagamento= data[5],
            servicos= data[6],
            medicamentos= medicamentos
        )

    def __parsedList(self, Consulta):
        listaConsulta = list(Consulta.read())
        clienteID = (listaConsulta[2].read())[0]
        listaConsulta[2] = clienteID
        animalID = (listaConsulta[3].read())[0]
        listaConsulta[3] = animalID
        veterinarioID = (listaConsulta[4].read())[0]
        listaConsulta[4] = veterinarioID
        servicosID = (listaConsulta[5].read())[0]
        listaConsulta[5] = servicosID
        pagamentoTipo = (listaConsulta[7].read())[0]
        listaConsulta[7] = pagamentoTipo

        listaMedicamentos = listaConsulta.pop(6)
        for i in range(len(listaMedicamentos)):
            produtoID = (listaMedicamentos[i][0].read())[0]
            listaMedicamentos[i][0] = produtoID
            listaMedicamentos[i].insert(0,listaConsulta[0])
        
        lista = [listaConsulta, listaMedicamentos]
        
        return lista

    def __init__(self, ClienteDAO, AnimalDAO, ProdutoDAO, VeterinarioDAO, PagamentoDAO, ServicoDAO):
        super().__init__('Consulta', 'IDConsulta')
        self.__ClienteDAO = ClienteDAO
        self.__AnimalDAO = AnimalDAO
        self.__ProdutoDAO = ProdutoDAO
        self.__VeterinarioDAO = VeterinarioDAO
        self.__PagamentoDAO = PagamentoDAO
        self.__ServicoDAO = ServicoDAO
    
    def add(self, Consulta):
        lista  = self.__parsedList(Consulta)
        t = db.execute(f'INSERT INTO Consulta VALUES (?,?,?,?,?,?,?)', lista[0])
        for medicamento in lista[1]:
            db.execute(f'INSERT INTO Consulta_Medicamentos (?,?,?)', medicamento)
        db.commit()
        return t

    def update(self, Consulta):
        lista = self.__parsedList(Consulta)

        db.execute(f'UPDATE Consulta SET DataConsulta = {lista[0][1]}, Dono = {lista[0][2]}, Animal = {lista[0][3]}, Veterinario = {lista[0][4]}, Pagamento = {lista[0][5]}, Servicos = {lista[0][6]} WHERE Codigo = {lista[0][0]}')
        
        #Não possui a função remover medicamento do Banco de Dados
        for medicamento in lista[1]:
            consulta_medicamento = []
            consulta_medicamento = db.record("SELECT * FROM Consulta_Medicamentos WHERE IDConsulta = ?, IDProduto = ?",(medicamento[0],medicamento[1]))
            if consulta_medicamento:
                db.execute(f'UPDATE Consulta_Medicamentos SET Quantidade = {medicamento[2]} WHERE IDConsulta = {medicamento[1]}, IDProduto = {medicamento[0]}')
            else:
                db.execute(f'INSERT INTO Consulta_Medicamentos (?,?,?)', medicamento)
        
        db.commit()

    def getByID(self, ID):
        consulta = super().getByID(ID)
        if not consulta:
            return None
        return self.__parseDataToObject(consulta)

    def getAll(self):
        consultas = super().getAll()
        parsedConsulta = []
        for consulta in consultas:
            parsedConsulta.append(self.__parseDataToObject(consulta))
        return parsedConsulta

    def getByAnimal(self, Animal):
        consultas = self.select('*', f'Animal = \'{Animal.read()[0]}\'')
        parsedConsulta = []
        for consulta in consultas:
            parsedConsulta.append(self.__parseDataToObject(consulta))
        return parsedConsulta
