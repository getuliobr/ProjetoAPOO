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

    def __init__(self, data, dono, animal, veterinario, pagamento, codigo = None, servicos = None, medicamentos = None):
        if not codigo:
            codigo = str(uuid4())
        self.codigo = codigo
        self.data = data
        self.dono = dono 
        self.animal = animal
        self.veterinario = veterinario
        self.pagamento = pagamento
        if(servicos):
            self.servicos = servicos
        if not medicamentos:
            self.medicamentos = []
        else:
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

    def addMedicamento(self, Produto):
        flag = -1
        i = 0
        for medicamento in self.medicamentos:
            if Produto.read()[0] == (medicamento[0].read())[0]:
                flag = i
                break
            i += 1

        if(flag != -1):
            self.medicamentos[flag][1] += 1
        else:
            self.medicamentos.append(Produto, 1)

    def removeMedicamento(self, Produto):
        i = 0
        for medicamento in self.medicamentos:
            if Produto.read()[0] == (medicamento[0].read())[0]:
                if(medicamento[1] > 1):
                    medicamento[1] -= 1
                else:
                    medicamento.pop(i)
            i += 1

    def read(self):
        return(self.data, self.dono, self.animal, self.veterinario, self.servicos, self.medicamentos, self.pagamento)