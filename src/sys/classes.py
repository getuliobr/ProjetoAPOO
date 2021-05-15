class Veterinario:

    def __init__(self, codigo, nome, endereco, cidade, estado, foneResidencia, foneCelular):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.foneResidencia = foneResidencia
        self.foneCelular = foneCelular
    
    def update(self, codigo= False, nome= False, endereco= False, cidade= False, estado= False, foneResidencia= False, foneCelular=False):
        if(codigo):
            self.codigo = codigo
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

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def update(self, codigo= False, nome= False):
        if(codigo):
            self.codigo = codigo
        if(nome):
            self.nome = nome
    
    def read(self):
        return(self.codigo, self.nome)

class Administrador:

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
    
    def update(self, codigo= False, nome= False):
        if(codigo):
            self.codigo = codigo
        if(nome):
            self.nome = nome
    
    def read(self):
        return (self.codigo, self.nome)