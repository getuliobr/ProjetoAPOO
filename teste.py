from src.sys.cliente import Cliente
from src.dao.DAOCliente import ClienteDAO
from src.db import db
from random import randint
from time import sleep
import math

db.build()

a = ClienteDAO()

nomes = []
with open('nomes.txt', 'r') as f:
  nomes = f.read().split('\n')


for i in range(100):
  primeiroNome = f'{nomes[randint(0, len(nomes) - 1)]}'
  sobreNome = f'{nomes[randint(0, len(nomes) - 1)]}'
  nome = f'{primeiroNome} {sobreNome} {nomes[randint(0, len(nomes) - 1)]}'
  telefone = randint(10000000000, 99999999999)
  cpf = randint(10000000000, 99999999999)
  email = f'{primeiroNome}{round(cpf/telefone)}@gmail.com'
  endereco = f'Rua {primeiroNome}, Numero {randint(1, 999)}, Bairro {sobreNome}'
  cidade = 'Campo Mourao'
  estado = 'Parana'
  
  novoCliente = Cliente(nome, endereco, cidade, estado, telefone, cpf, email)
  a.add(novoCliente)

