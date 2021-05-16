from random import randint
from time import sleep
import math

from src.db import db

from src.sys.pagamento import Pagamento
from src.sys.produto import CategoriaDeProduto
from src.sys.cliente import Cliente, Animal, Especie, Raca

from src.dao.DAOProduto import CategoriaDeProdutoDAO
from src.dao.DAOCliente import ClienteDAO, AnimalDAO, EspecieDAO, RacaDAO
from src.dao.DAOPagamento import PagamentoDAO

db.build()

'''
ClienteDAO = ClienteDAO()
EspecieDAO = EspecieDAO()
RacaDAO = RacaDAO()
AnimalDAO = AnimalDAO(ClienteDAO, EspecieDAO, RacaDAO)

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
  ClienteDAO.add(novoCliente)

clientes = ClienteDAO.getAll()

cachorro = Especie('cachorro')
gato = Especie('gato')

EspecieDAO.add(cachorro)
EspecieDAO.add(gato)

branco = Raca('branco')
preto = Raca('preto')
cinza = Raca('cinza')

RacaDAO.add(branco)
RacaDAO.add(preto)
RacaDAO.add(cinza)

racas = [branco, preto, cinza]

for i in range(100):
  cliente = clientes[randint(0, len(clientes) - 1)]
  nome = f'{nomes[randint(0, len(nomes) - 1)]}'
  nasc = f'{randint(1, 30)}/{randint(1, 12)}/{randint(2015, 2020)}'

  especie = gato
  if randint(1, 100) > 50:
    especie = cachorro

  sexo = 'm'
  if randint(1, 100) > 50:
    sexo = 'f'

  a = Animal(nome, cliente, nasc, especie, racas[randint(0, 2)], sexo, 'roxo')
  AnimalDAO.add(a)

print(AnimalDAO.getAll())
'''

'''
PagamentoDAO = PagamentoDAO()
cartao = Pagamento('cartao')
cheque = Pagamento('cheque')
dinheiro = Pagamento('dinheiro')
valePresente = Pagamento('vale presente')

PagamentoDAO.add(cartao)
PagamentoDAO.add(cheque)
PagamentoDAO.add(dinheiro)
PagamentoDAO.add(valePresente)
pagamentos = PagamentoDAO.getAll()

print(pagamentos)
print(pagamentos[0].read())
print(PagamentoDAO.getByType('cartao').read())
'''

'''
CategoriaDeProdutoDAO = CategoriaDeProdutoDAO()

racao = CategoriaDeProduto('ração')
remedio = CategoriaDeProduto('remedio')
brinquedo = CategoriaDeProduto('brinquedo')

CategoriaDeProdutoDAO.add(racao)
CategoriaDeProdutoDAO.add(remedio)
CategoriaDeProdutoDAO.add(brinquedo)

print(len(CategoriaDeProdutoDAO.getAll()))

print(CategoriaDeProdutoDAO.getByName('remedio')[0].read())

print(CategoriaDeProdutoDAO.getByID('249296a1-4429-4c38-a088-bc56099f1e31').read())
'''
