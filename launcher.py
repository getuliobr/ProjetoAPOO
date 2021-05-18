
from time import sleep
from src.db import db
import os

from src.sys.pagamento import Pagamento
from src.sys.produto import CategoriaDeProduto, Produto
from src.sys.cliente import Cliente, Animal, Especie, Raca
from src.sys.consulta import Servico, Consulta
from src.sys.classes import Atendente, Veterinario

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

class AdministradorFuncional():
  def __init__(self):
    self.__menu()
  
  def __menu(self):
    logado = True
    while logado:
      os.system('cls||clear')
      print('Escolha um submenu')
      print('1 - Atendente')
      print('2 - Veterinario')
      print('3 - Categoria Produtos')
      print('4 - Produtos')
      print('0 - Sair')
      opcao = int(input('Digite o submenu: '))
      if opcao == 0:
        logado = False
      if opcao == 1:
        self.__menuAtendente()
      if opcao == 2:
        self.__menuVeterinario()
      if opcao == 3:
        self.__menuCategoriaProdutos()
      if opcao == 4:
        self.__menuProdutos()

  def __menuProdutos(self):
    os.system('cls||clear')
    print('1 - Cadastrar Produto')
    print('2 - Ler')
    opcao = int(input('Digite o submenu: '))
    if opcao == 1:
      self.__cadastrarProduto()
    if opcao == 2:
      self.__lerProdutos()

  def __escolherProdutos(self):
    os.system('cls||clear')
    produtos = ProdutoDAO.getAll()
    i = 0
    for produto in produtos:
      print(i, '-', produto.read()[1])
      i += 1
    codigo = int(input('Qual codigo do produto? '))
    if codigo >= 0 or codigo < len(produtos):
      return produtos[codigo]
    return None

  def __lerProdutos(self):
    produto = self.__escolherProdutos()
    os.system('cls||clear')
    id, descricao, fabricante, categoria, preco = produto.read()
    print(f'Produto com ID: {id} da categoria {categoria.read()[1]}\nTem descricao: {descricao}\nE fabricado por: {fabricante}\nE tem preço: {preco}')    
    input('Aperte enter para continuar ...')

  def __cadastrarProduto(self):
    descricao = input('Descricao: ')
    fabricante = input('Fabricante: ')
    preco = float(input('Preco: '))
    categoria = self.__escolherCategoriaProdutos()
    produto = Produto(descricao, fabricante, categoria, preco)
    ProdutoDAO.add(produto)

  def __menuCategoriaProdutos(self):
    os.system('cls||clear')
    print('1 - Cadastrar')
    print('2 - Ler')
    print('3 - Remover')
    opcao = int(input('Digite o submenu: '))
    if opcao == 1:
      self.__cadastrarCategoriaProdutos()
    if opcao == 2:
      self.__lerCategoriaProdutos()
    if opcao == 3:
      self.__removerCategoriaProdutos()

  def __cadastrarCategoriaProdutos(self):
    os.system('cls||clear')
    nome = input('Nome categoria: ')
    cat = CategoriaDeProduto(nome)
    CategoriaDeProdutoDAO.add(cat)

  def __escolherCategoriaProdutos(self):
    categorias = CategoriaDeProdutoDAO.getAll()
    i = 0
    for categoria in categorias:
      print(i, '-', categoria.read()[1])
      i += 1
    codigo = int(input('Qual codigo da categoria? '))
    os.system('cls||clear')
    if codigo >= 0 or codigo < len(categorias):
      return categorias[codigo]
    return None

  def __lerCategoriaProdutos(self):
    os.system('cls||clear')
    categoria = self.__escolherCategoriaProdutos()
    id, nome = categoria.read()
    print(f'Categoria com ID: {id}\nTem o nome: {nome}')
    print(f'Opcao:\n1 - Deletar Categoria')
    opcao = int(input('Digite o submenu: '))
    if opcao == 1:
      self.__removerCategoriaProdutos(categoria)

  def __removerCategoriaProdutos(self, categoria = None):
    os.system('cls||clear')
    if categoria == None:
      categoria = self.__escolherCategoriaProdutos()
    id = categoria.read()[0]
    CategoriaDeProdutoDAO.deleteByID(id)

  def __menuAtendente(self):
    os.system('cls||clear')
    print('Menu Atendente')
    print('1 - Cadastrar')
    print('2 - Ler')
    print('3 - Atualizar')
    print('4 - Remover')
    opcao = int(input('Digite o submenu: '))
    if opcao == 1:
      self.__cadastrarAtendente()
    if opcao == 2:
      self.__lerAtendente()
    if opcao == 3:
      self.__atualizarAtendente()
    if opcao == 4:
      self.__removerAtendente()

  def __menuVeterinario(self):
    os.system('cls||clear')
    print('Menu Atendente')
    print('1 - Cadastrar')
    print('2 - Ler')
    print('3 - Atualizar')
    print('4 - Remover')
    opcao = int(input('Digite o submenu: '))
    if opcao == 1:
      self.__adicionarVeterinario()
    if opcao == 2:
      self.__lerVeterinario()
    if opcao == 3:
      self.__atualizarVeterinario()
    if opcao == 4:
      self.__removerVeterinario()

  def __cadastrarAtendente(self):
    nome = input('Nome atendente: ')
    c = Atendente(nome)
    AtendenteDAO.add(c)

  def __atualizarAtendente(self, atendente = None):
    if atendente == None:
      atendente = self.__escolherAtendente()
    if atendente:
      id, nome = atendente.read()
      print("Deixe vazio para não alterar")
      nome = input('Nome do Atendente: ') or nome
      atendente.update(nome)
      AtendenteDAO.update(atendente)

  def __removerAtendente(self, atendente = None):
    if atendente == None:
      atendente = self.__escolherAtendente()
    if atendente:
      id, nome = atendente.read()
      AtendenteDAO.deleteByID(id)

  def __lerAtendente(self):
    atendente = self.__escolherAtendente()
    id, nome = atendente.read()
    print(f'Atendente com ID: {id}\nTem o nome: {nome}')
    print(f'Opcao:\n1 - Atualizar Atendente\n2 - Deletar Atendente')
    opcao = int(input('Digite o submenu: '))
    if opcao == 1:
      self.__atualizarAtendente(atendente)
    if opcao == 2:
      self.__removerAtendente(atendente)

  def __escolherAtendente(self):
    os.system('cls||clear')
    atendentes = AtendenteDAO.getAll()
    i = 0
    for atendente in atendentes:
      print(i, '-', atendente.read()[1])
      i += 1
    codigo = int(input('Qual codigo do cliente? '))
    os.system('cls||clear')
    if codigo >= 0 or codigo < len(atendentes):
      return atendentes[codigo]
    return None

  def __adicionarVeterinario(self):
    nome = input('Nome: ')
    endereco = input('Endereço: ')
    cidade = input('Cidade: ')
    estado = input('Estado: ')
    foneResidencia = input('Telefone Residencia: ')
    foneCelular = input('Telefone Celular: ')
    vet = Veterinario(nome, endereco, cidade, estado, foneResidencia, foneCelular)
    VeterinarioDAO.add(vet)

  def __escolherVeterinario(self):
    os.system('cls||clear')
    veterinarios = VeterinarioDAO.getAll()
    i = 0
    for veterinario in veterinarios:
      print(i, '-', veterinario.read()[1])
      i += 1
    codigo = int(input('Qual codigo do cliente? '))
    os.system('cls||clear')
    if codigo >= 0 or codigo < len(veterinarios):
      return veterinarios[codigo]
    return None

  def __lerVeterinario(self):
    veterinario = self.__escolherVeterinario()
    id, nome, endereco, cidade, estado, foneResidencia, foneCelular = veterinario.read()
    print(f'Veterinario com ID: {id}\nTem o nome: {nome}\nMora no endereço {endereco}, {cidade}, {estado}')
    print(f'Tem os seguintes telefones: {foneResidencia}, {foneCelular}')
    print(f'Opcao:\n1 - Atualizar Veterinario\n2 - Deletar Veterinario')
    opcao = int(input('Digite o submenu: '))
    if opcao == 1:
      self.__atualizarVeterinario(veterinario)
    if opcao == 2:
      self.__removerVeterinario(veterinario)

  def __atualizarVeterinario(self, veterinario = None):
    if veterinario == None:
      veterinario = self.__escolherAtendente()
    if veterinario:
      id, nome, endereco, cidade, estado, foneResidencia, foneCelular = veterinario.read()
      print('Para nao alterar o campo aperte enter')
      nome = input('Nome: ') or nome
      endereco = input('Endereço: ') or endereco
      cidade = input('Cidade: ') or cidade
      estado = input('Estado: ') or estado
      foneResidencia = input('Telefone Residencia: ') or foneResidencia
      foneCelular = input('Telefone Celular: ') or foneCelular
      veterinario.update(nome, endereco, cidade, estado, foneResidencia, foneCelular)
      VeterinarioDAO.update(veterinario)

  def __removerVeterinario(self, veterinario = None):
    if veterinario == None:
      veterinario = self.__escolherAtendente()
    if veterinario:
      id = veterinario.read()[0]
      VeterinarioDAO.deleteByID(id)

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
      print('5 - Venda')
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
      if opcao == 4:
        self.__menuAnimal()

  def __menuAnimal(self):
    print('1 - Criar')
    print('2 - Ler')
    print('0 - Sair')
    opcao = int(input('Digite a opcao: '))
    if opcao == 1:
      self.__criarAnimal()
    if opcao == 2:
      self.__lerAnimal()

  def __criarAnimal(self):
    nome = input('Nome do Animal: ')
    dataNascimento = input('Data de Nascimento do Animal: ')
    sexo = input('Sexo do Animal: ')
    cor = input('Cor do Animal: ')
    dono = self.__escolherCliente()
    raca = self.__escolherRaca()
    especie = self.__escolherEspecie()
    animal = Animal(nome, dono, dataNascimento, especie, raca, sexo, cor)
    AnimalDAO.add(animal)

  def __lerAnimal(self): ### erro ler animal
    animal = self.__escolherAnimal()
    nome, dono, dataNascimento, especie, raca, sexo, cor = animal.read()
    print(f'Animal com nome {nome} do dono: {dono.read()[1]}')
    print(f'Nascido em {dataNascimento}')
    print(f'Da especie {especie.read()[1]}')
    print(f'Da raca {raca.read()[1]}')
    print(f'Do sexo {sexo}')
    print(f'Da cor {cor}')
    input('Aperte enter para continuar ...')

  def __escolherAnimal(self):
    animais = ClienteDAO.getAll()
    i = 0
    for animal in animais:
      nome = animal.read()[1]
      dono = animal.read()[2]
      nomeDono = dono.read()[1]
      print(i, '-', nome, '-', nomeDono)
      i += 1
    codigo = int(input('Qual codigo do animal? '))
    os.system('cls||clear')
    if codigo >= 0 or codigo < len(animais):
      return animais[codigo]
    return None

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
  print('2 - Adminisitrador')
  print('3 - Sair')
  cargo = int(input('Escolha seu cargo: '))
  if cargo == 1:
    AtendenteFuncional()
  if cargo == 2:
    AdministradorFuncional()
  if cargo == 3:
    os.system('cls||clear')
    rodar = False