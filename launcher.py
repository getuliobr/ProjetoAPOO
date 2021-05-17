
from time import sleep
from src.db import db
import os

from src.sys.pagamento import Pagamento
from src.sys.produto import CategoriaDeProduto, Produto
from src.sys.cliente import Cliente, Animal, Especie, Raca
from src.sys.consulta import Servico, Consulta
from src.sys.classes import Veterinario

from src.dao.DAOProduto import CategoriaDeProdutoDAO, ProdutoDAO
from src.dao.DAOCliente import ClienteDAO, AnimalDAO, EspecieDAO, RacaDAO
from src.dao.DAOPagamento import PagamentoDAO
from src.dao.DAOClasses import VeterinarioDAO, AtendenteDAO, AdministradorDAO
from src.dao.DAOConsulta import ConsultaDAO, ServicoDAO

CategoriaDeProdutoDAO = CategoriaDeProdutoDAO()
ProdutoDAO = ProdutoDAO(CategoriaDeProdutoDAO)
ClienteDAO = ClienteDAO()
EspecieDAO = EspecieDAO()
RacaDAO = RacaDAO()
AnimalDAO = AnimalDAO(ClienteDAO, EspecieDAO, RacaDAO)
PagamentoDAO = PagamentoDAO()
VeterinarioDAO = VeterinarioDAO()
ServicoDAO = ServicoDAO()
ConsultaDAO = ConsultaDAO(ClienteDAO, AnimalDAO, ProdutoDAO, VeterinarioDAO, PagamentoDAO, ServicoDAO)
AtendenteDAO = AtendenteDAO()
AdministradorDAO = AdministradorDAO()

class AtendenteFuncional:
  def __init__(self):
    os.system('cls||clear')
    atendentes = AtendenteDAO.getAll()
    i = 0
    print('Qual atendente voce e?')
    for atendente in atendentes:
      name = atendente.read()[1]
      print(i, '-', name)
    codigo = int(input('Qual seu codigo? '))
    if codigo >= 0 or codigo < len(atendentes):
      self.atendente = atendentes[codigo]
      self.__menu()

  def __menu(self):
    logado = True
    while logado:
      os.system('cls||clear')
      print('Escolha um submenu')
      print('1 - Cliente')
      print('2 - Raca')
      print('3 - Especie')
      print('4 - Animal')
      print('5 - Consulta')
      print('6 - Venda')
      print('0 - Sair')
      opcao = int(input('Digite o submenu: '))
      if opcao == 0:
        logado = False
      if opcao == 1:
        self.__menuCliente()
      if opcao == 2:
        self.__menuRaca()
      if opcao == 3:
        self.__menuEspecie()

  def __escolherCliente(self):
    clientes = ClienteDAO.getAll()
    i = 0
    for cliente in clientes:
      print(i, '-', cliente.read()[1])
      i += 1
    codigo = int(input('Qual codigo do cliente? '))
    os.system('cls||clear')
    if codigo >= 0 or codigo < len(clientes):
      return clientes[codigo]
    return None

  def __menuCrud(self):
    os.system('cls||clear')
    print('Menu Cliente')
    print('1 - Cadastrar')
    print('2 - Ler')
    print('3 - Atualizar')
    print('4 - Remover')
    return  int(input('Digite a opcao: '))

  def __menuRaca(self):
    os.system('cls||clear')
    print('Menu Cliente')
    print('1 - Cadastrar')
    print('2 - Ler')
    print('3 - Remover')
    opcao = int(input('Digite a opcao: '))
    if opcao == 1:
      self.__cadastrarRaca()
    if opcao == 2:
      self.__lerRaca()
    if opcao == 3:
      self.__removerRaca()

  def __menuEspecie(self):
    os.system('cls||clear')
    print('Menu Cliente')
    print('1 - Cadastrar')
    print('2 - Ler')
    print('3 - Remover')
    opcao = int(input('Digite a opcao: '))
    if opcao == 1:
      self.__cadastrarEspecie()
    if opcao == 2:
      self.__lerEspecie()
    if opcao == 3:
      self.__removerEspecie()

  def __cadastrarEspecie(self):
    nome = input('Nome da especie: ')
    nome = Especie(nome)
    EspecieDAO.add(nome)

  def __escolherEspecie(self):
    especies = EspecieDAO.getAll()
    i = 0
    for especie in especies:
      print(i, '-', especie.read()[1])
      i += 1
    codigo = int(input('Qual codigo da especie? '))
    os.system('cls||clear')
    if codigo >= 0 or codigo < len(especies):
      return especies[codigo]
    return None

  def __lerEspecie(self):
    os.system('cls||clear')
    especie = self.__escolherEspecie()
    codigo, nome = especie.read()
    print(f'Especie com codigo {codigo}\nTem nome: {nome}')
    opcao = int(input('Deseja remover essa especie?\n0 - Nao\n1 - Sim\nOpcao: '))
    if opcao == 1:
      self.__removerEspecie(especie)

  def __removerEspecie(self, especie = None):
    if especie == None:
      especie = self.__escolherEspecie()
    id = especie.read()[0]
    EspecieDAO.deleteByID(id)

  def __lerRaca(self):
    os.system('cls||clear')
    raca = self.__escolherRaca()
    codigo, descricao = raca.read()
    print(f'Raca com codigo {codigo}\nTem descricao: {descricao}')
    opcao = int(input('Deseja remover essa raca?\n0 - Nao\n1 - Sim\nOpcao: '))
    if opcao == 1:
      self.__removerRaca(raca)

  def __removerRaca(self, raca = None):
    if raca == None:
      raca = self.__escolherRaca()
    id = raca.read()[0]
    RacaDAO.deleteByID(id)

  def __escolherRaca(self):
    racas = RacaDAO.getAll()
    i = 0
    for raca in racas:
      print(i, '-', raca.read()[1])
      i += 1
    codigo = int(input('Qual codigo da raca? '))
    os.system('cls||clear')
    if codigo >= 0 or codigo < len(racas):
      return racas[codigo]
    return None

  def __cadastrarRaca(self):
    descricao = input('Descricao da raca: ')
    raca = Raca(descricao)
    RacaDAO.add(raca)

  def __menuCliente(self):
    opcao = self.__menuCrud()
    if opcao == 1:
      self.__cadastrarCliente()
    if opcao == 2:
      self.__lerCliente()
    if opcao == 3:
      self.__atualizarCliente()
    if opcao == 4:
      self.__removerCliente()

  def __removerCliente(self, cliente = None):
    if cliente == None:
      cliente = self.__escolherCliente()
    if cliente:
      id = cliente.read()[0]
      ClienteDAO.deleteByID(id)

  def __atualizarCliente(self, cliente = None):
    if cliente == None:
      cliente = self.__escolherCliente()
    if cliente:
      id, nome, endereco, cidade, estado, telefone, documento, email = cliente.read()
      print("Deixe vazio para não alterar")
      nome = input('Nome do Cliente: ') or nome
      endereco = input('Endereço do Cliente: ') or endereco
      cidade = input('Cidade do Cliente: ') or cidade
      estado = input('Estado do Cliente: ') or estado
      telefone = input('Telefone do Cliente: ') or telefone
      documento = input('CPF do Cliente: ') or documento
      email = input('EMail do Cliente: ') or email
      cliente.update(nome, endereco, cidade, estado, telefone, documento, email)
      ClienteDAO.update(cliente)

  def __lerCliente(self):
    os.system('cls||clear')
    cliente = self.__escolherCliente()
    if cliente:
      id, nome, endereco, cidade, estado, telefone, documento, email = cliente.read()
      print(f'Cliente com ID: {id}')
      print(f'Tem o nome: {nome}')
      print(f'Mora no seguinte endereço: {endereco}, {cidade}, {estado}')
      print(f'Tem o documento: {documento}')
      print(f'Tem o telefone: {telefone}')
      print(f'E tem o email: {email}')

      print('Deseja realizar alguma atividade com esse cliente?')
      print('0 - Sair')
      print('1 - Atualizar')
      print('2 - Deletar')
      opcao = int(input('Digite a opcao: '))
      if opcao == 1:
        self.__atualizarCliente(cliente)
      if opcao == 2:
        self.__removerCliente(cliente)

  def __cadastrarCliente(self):
    os.system('cls||clear')
    nome = input('Nome do Cliente: ')
    endereco = input('Endereço do Cliente: ')
    cidade = input('Cidade do Cliente: ')
    estado = input('Estado do Cliente: ')
    telefone = input('Telefone do Cliente: ')
    documento = input('CPF do Cliente: ')
    email = input('EMail do Cliente: ')
    cliente = Cliente(nome, endereco, cidade, estado, telefone, documento, email)
    ClienteDAO.add(cliente)

rodar = True
while rodar:
  os.system('cls||clear')
  print('Qual é seu cargo?')
  print('1 - Atendente')
  print('2 - Veterinario')
  print('3 - Adminisitrador')
  print('4 - Sair')
  cargo = int(input('Escolha seu cargo: '))
  if cargo == 1:
    AtendenteFuncional()
  if cargo == 4:
    os.system('cls||clear')
    rodar = False