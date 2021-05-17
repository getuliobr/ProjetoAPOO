from src.sys.produto import Produto
from uuid import uuid4

class Servico:

    def __init__(self, descricao, preco, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco

    def update(self, descricao= False, preco= False):
        if(descricao):
            self.descricao = descricao
        if(preco):
            self.preco = descricao
    
    def read(self):
        return(self.codigo, self.descricao, self.preco)


class Consulta:

    def __init__(self, data, dono, animal, veterinario, pagamento, codigo = None, servicos = None, medicamentos = []):
        if not codigo:
            codigo = str(uuid4())
        self.codigo = codigo
        self.data = data
        self.dono = dono 
        self.animal = animal
        self.veterinario = veterinario
        self.pagamento = pagamento
        self.servicos = servicos
        self.medicamentos = medicamentos

    def update(self, data= False, dono= False, animal= False, veterinario= False, servicos= False, pagamento= False):
        if(data):
            self.data = data
        if(dono):
            self.dono = dono
        if(animal):
            self.animal = animal
        if(veterinario):
            self.veterinario = veterinario
        if(servicos):
            self.servicos = servicos
        if(pagamento):
            self.pagamento = pagamento

    def addMedicamento(self, Produto, quantidade = 1):
        flag = -1
        i = 0
        for medicamento in self.medicamentos:
            print('medicamento', medicamento)
            if Produto.read()[0] == (medicamento[0].read())[0]:
                flag = i
                break
            i += 1

        if(flag != -1):
            self.medicamentos[flag][1] += quantidade
        else:
            self.medicamentos.append([Produto, quantidade])

    def read(self):
        return(self.codigo, self.data, self.dono, self.animal, self.veterinario, self.pagamento, self.servicos, self.medicamentos)