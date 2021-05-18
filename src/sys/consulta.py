from src.sys.produto import Produto
from uuid import uuid4

class Servico:

    def __init__(self, descricao, preco, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco

    def update(self, descricao= False, preco= False):
        if(descricao):
            self.__descricao = descricao
        if(preco):
            self.__preco = descricao
    
    def read(self):
        return(self.__codigo, self.__descricao, self.__preco)


class Consulta:

    def __init__(self, data, dono, animal, veterinario, pagamento, codigo = None, servicos = None, medicamentos = []):
        if not codigo:
            codigo = str(uuid4())
        self.__codigo = codigo
        self.__data = data
        self.__dono = dono 
        self.__animal = animal
        self.__veterinario = veterinario
        self.__pagamento = pagamento
        self.__servicos = servicos
        self.__medicamentos = medicamentos

    def update(self, data= False, dono= False, animal= False, veterinario= False, servicos= False, pagamento= False):
        if(data):
            self.__data = data
        if(dono):
            self.__dono = dono
        if(animal):
            self.__animal = animal
        if(veterinario):
            self.__veterinario = veterinario
        if(servicos):
            self.__servicos = servicos
        if(pagamento):
            self.__pagamento = pagamento

    def addMedicamento(self, Produto, quantidade = 1):
        flag = -1
        i = 0
        for i in range(len(self.__medicamentos)):
            if Produto.read()[0] == (self.__medicamentos[i][0].read())[0]:
                flag = i
                break
            i += 1

        if(flag != -1):
            self.__medicamentos[flag][1] += quantidade
        else:
            self.__medicamentos.append([Produto, quantidade])

    def read(self):
        return(self.__codigo, self.__data, self.__dono, self.__animal, self.__veterinario, self.__pagamento, self.__servicos, self.__medicamentos)