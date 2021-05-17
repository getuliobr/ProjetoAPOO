from random import randint
from time import sleep
import math
from src.dao.DAOClasses import VeterinarioDAO
from src.dao.DAOConsulta import ConsultaDAO, ServicoDAO

from src.db import db

from src.sys.pagamento import Pagamento
from src.sys.produto import CategoriaDeProduto, Produto
from src.sys.cliente import Cliente, Animal, Especie, Raca

from src.dao.DAOProduto import CategoriaDeProdutoDAO, ProdutoDAO
from src.dao.DAOCliente import ClienteDAO, AnimalDAO, EspecieDAO, RacaDAO
from src.dao.DAOPagamento import PagamentoDAO
from src.sys.consulta import Servico, Consulta
from src.sys.classes import Veterinario

db.build()

ClienteDAO = ClienteDAO()
EspecieDAO = EspecieDAO()
RacaDAO = RacaDAO()
AnimalDAO = AnimalDAO(ClienteDAO, EspecieDAO, RacaDAO)

nomes = []
with open('nomes.txt', 'r') as f:
  nomes = f.read().split('\n')


for i in range(10):
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

for i in range(10):
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



PagamentoDAO = PagamentoDAO()

cartao = Pagamento('cartao')
cheque = Pagamento('cheque')
dinheiro = Pagamento('dinheiro')
valePresente = Pagamento('vale presente')

# PagamentoDAO.add(cartao)
# PagamentoDAO.add(cheque)
# PagamentoDAO.add(dinheiro)
# PagamentoDAO.add(valePresente)
# pagamentos = PagamentoDAO.getAll()


CategoriaDeProdutoDAO = CategoriaDeProdutoDAO()


# racao = CategoriaDeProduto('ração')
# remedio = CategoriaDeProduto('remedio')
# brinquedo = CategoriaDeProduto('brinquedo')

# CategoriaDeProdutoDAO.add(racao)
# CategoriaDeProdutoDAO.add(remedio)
# CategoriaDeProdutoDAO.add(brinquedo)

ProdutoDAO = ProdutoDAO(CategoriaDeProdutoDAO)

categoria = CategoriaDeProdutoDAO.getAll()[0]


ServicoDAO = ServicoDAO()

# exame = Servico('exame', 50)
# raiox = Servico('raio x', 50)

VeterinarioDAO = VeterinarioDAO()

veterinario = Veterinario('veterinario brabo', 'rua', 'cidade', 'estado', '98765432100', '98765432100')
VeterinarioDAO.add(veterinario)

ConsultaDAO = ConsultaDAO(ClienteDAO, AnimalDAO, ProdutoDAO, VeterinarioDAO, PagamentoDAO, ServicoDAO)
cliente = ClienteDAO.getByID('c3e3b9c3-4028-4982-84f7-1b5bc18876f1')

animal = AnimalDAO.getClientAnimals(cliente)[0]

pagamento = PagamentoDAO.getAll()[0]

servico = ServicoDAO.getAll()[0]



consulta = Consulta('2020/12/25', cliente, animal, veterinario, pagamento, servicos=servico)

produto = ProdutoDAO.getAll()[0]

testeDengue = Produto('teste da dengue', 'butantan', CategoriaDeProdutoDAO.getAll()[0], 1337)

print(produto.read())

ProdutoDAO.add(testeDengue)

consulta.addMedicamento(produto)
consulta.addMedicamento(testeDengue)
consulta.addMedicamento(testeDengue)
consulta.addMedicamento(testeDengue)
consulta.addMedicamento(testeDengue)


ConsultaDAO.add(consulta)

print('teste')
consulta = ConsultaDAO.getByID('12b4026a-cc8e-4f80-8f09-1a309bb871b3').addMedicamento(testeDengue)
ConsultaDAO.update(consulta)
