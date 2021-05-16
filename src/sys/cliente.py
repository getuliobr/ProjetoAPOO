from . import db

class Cliente:
    
    def __init__(self, codigo, nome, endereco, cidade, estado, telefone, documento, email):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.telefone = telefone
        self.documento = documento
        self.email = email

    def update(self, codigo= False , nome= False, endereco= False, cidade= False, estado= False, telefone= False, documento= False, email= False):
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
        if(telefone):
            self.telefone = telefone
        if(documento):
            self.documento = documento
        if(email):
            self.email = email
    
    def read(self):
        return (self.codigo, self.nome, self.endereco, self.cidade, self.estado, self.telefone, self.documento, self.email)
    

class Animal:

    def __init__(self, codigo, nome, dono, dataNascimento, especie, raca, sexo, cor):
        self.codigo = codigo
        self.nome = nome
        self.dono = dono
        self.dataNascimento = dataNascimento
        self.especie = especie
        self.raca = raca
        self.sexo = sexo
        self.cor = cor

    def update(self, codigo= False, nome= False, dono= False, dataNascimento= False, especie= False, raca= False, sexo= False, cor= False):
        if(codigo):
            self.codigo = codigo
        if(nome):
            self.nome = nome
        if(dono):
            self.dono = dono
        if(dataNascimento):
            self.dataNascimento = dataNascimento
        if(especie):
            self.especie = especie
        if(raca):
            self.raca = raca
        if(sexo):
            self.sexo = sexo
        if(cor):
            self.cor = cor
    
    def read(self):
        return(self.codigo, self.nome, self.dono, self.dataNascimento, self.especie, self.raca, self.sexo, self.cor)


class Especie:

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

class Raca:

    def __init__(self, codigo, descricao):
        self.codigo = codigo
        self.descricao = descricao

    def update(self, codigo= False, descricao= False):
        if(codigo):
            self.codigo = codigo
        if(descricao):
            self.descricao = descricao
    
    def read(self):
        return(self.codigo, self.descricao)