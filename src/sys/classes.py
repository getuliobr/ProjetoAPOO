from uuid import uuid4

class Veterinario:

    def __init__(self, nome, endereco, cidade, estado, foneResidencia, foneCelular, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.foneResidencia = foneResidencia
        self.foneCelular = foneCelular
    
    def update(self, nome= False, endereco= False, cidade= False, estado= False, foneResidencia= False, foneCelular=False):
        if(nome):
            self.nome = nome
        if(endereco):
            self.endereco = endereco
        if(cidade):
            self.cidade = cidade
        if(estado):
            self.estado = estado
        if(self.foneResidencia):
            self.foneResidencia = foneResidencia
        if(foneCelular):
            self.foneCelular = foneCelular
    
    def read(self):
        return (self.codigo, self.nome, self.endereco, self.cidade, self.estado, self.foneResidencia, self.foneCelular)

class Atendente:

    def __init__(self, nome, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.codigo = codigo
        self.nome = nome

    def update(self, nome= False):
        if(nome):
            self.nome = nome
    
    def read(self):
        return(self.codigo, self.nome)

class Administrador:

    def __init__(self, nome, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.codigo = codigo
        self.nome = nome
    
    def update(self, nome= False):
        if(nome):
            self.nome = nome
    
    def read(self):
        return (self.codigo, self.nome)