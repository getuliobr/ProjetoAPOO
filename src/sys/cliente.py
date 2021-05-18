from uuid import uuid4


class Cliente:
    
    def __init__(self, nome, endereco, cidade, estado, telefone, documento, email, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.__codigo = codigo
        self.__nome = nome
        self.__endereco = endereco
        self.__cidade = cidade
        self.__estado = estado
        self.__telefone = telefone
        self.__documento = documento
        self.__email = email

    def update(self, nome= False, endereco= False, cidade= False, estado= False, telefone= False, documento= False, email= False):
        if(nome):
            self.__nome = nome
        if(endereco):
            self.__endereco = endereco
        if(cidade):
            self.__cidade = cidade
        if(estado):
            self.__estado = estado
        if(telefone):
            self.__telefone = telefone
        if(documento):
            self.__documento = documento
        if(email):
            self.__email = email
    
    def read(self):
        return (self.__codigo, self.__nome, self.__endereco, self.__cidade, self.__estado, self.__telefone, self.__documento, self.__email)

class Animal:

    def __init__(self, nome, dono, dataNascimento, especie, raca, sexo, cor, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.__codigo = codigo
        self.__nome = nome
        self.__dono = dono
        self.__dataNascimento = dataNascimento
        self.__especie = especie
        self.__raca = raca
        self.__sexo = sexo
        self.__cor = cor

    def update(self, nome= False, dono= False, dataNascimento= False, especie= False, raca= False, sexo= False, cor= False):
        if(nome):
            self.__nome = nome
        if(dono):
            self.__dono = dono
        if(dataNascimento):
            self.__dataNascimento = dataNascimento
        if(especie):
            self.__especie = especie
        if(raca):
            self.__raca = raca
        if(sexo):
            self.__sexo = sexo
        if(cor):
            self.__cor = cor
    
    def read(self):
        return(self.__codigo, self.__nome, self.__dono, self.__dataNascimento, self.__especie, self.__raca, self.__sexo, self.__cor)

class Especie:

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

class Raca:

    def __init__(self, descricao, codigo = None):
        if not codigo:
            codigo = str(uuid4())
        self.__codigo = codigo
        self.__descricao = descricao

    def update(self, descricao= False):
        if(descricao):
            self.__descricao = descricao
    
    def read(self):
        return(self.__codigo, self.__descricao)