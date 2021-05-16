from src.sys.produto import Produto
from uuid import uuid4

class Consulta:

    def __init__(self, data, dono, animal, veterinario, pagamento, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.codigo = codigo
        self.data = data
        self.dono = dono 
        self.animal = animal
        self.veterinario = veterinario
        self.pagamento = pagamento

    def update(self, data= False, dono= False, animal= False, veterinario= False, servicos= False, medicamentos= False, pagamento= False):
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
        if(medicamentos):
            self.medicamentos = medicamentos
        if(pagamento):
            self.pagamento = pagamento

    def read(self):
        return(self.data, self.dono, self.animal, self.veterinario, self.servicos, self.medicamentos, self.pagamento)

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