from uuid import uuid4

class Veterinario:

    def __init__(self, nome, endereco, cidade, estado, foneResidencia, foneCelular, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.__codigo = codigo
        self.__nome = nome
        self.__endereco = endereco
        self.__cidade = cidade
        self.__estado = estado
        self.__foneResidencia = foneResidencia
        self.__foneCelular = foneCelular
    
    def update(self, nome= False, endereco= False, cidade= False, estado= False, foneResidencia= False, foneCelular=False):
        if(nome):
            self.__nome = nome
        if(endereco):
            self.__endereco = endereco
        if(cidade):
            self.__cidade = cidade
        if(estado):
            self.__estado = estado
        if(foneResidencia):
            self.__foneResidencia = foneResidencia
        if(foneCelular):
            self.__foneCelular = foneCelular
    
    def read(self):
        return (self.__codigo, self.__nome, self.__endereco, self.__cidade, self.__estado, self.__foneResidencia, self.__foneCelular)

class Atendente:

    def __init__(self, nome, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.__codigo = codigo
        self.__nome = nome

    def update(self, nome= False):
        if(nome):
            self.__nome = nome
    
    def read(self):
        return(self.__codigo, self.__nome)

class Administrador:

    def __init__(self, nome, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.__codigo = codigo
        self.__nome = nome
    
    def update(self, nome= False):
        if(nome):
            self.__nome = nome
    
    def read(self):
        return (self.__codigo, self.__nome)