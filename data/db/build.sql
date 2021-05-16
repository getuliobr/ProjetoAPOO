CREATE TABLE IF NOT EXISTS Veterinario(
    Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome varchar(40),
    Endereco varchar(60),
    Cidade varchar(20),
    Estado varchar(15),
    FoneResidencia varchar(30),
    FoneCelular varchar(30)
);
CREATE TABLE IF NOT EXISTS Atendente(
    Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome varchar(40)
);

CREATE TABLE IF NOT EXISTS Administrador(
    Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome varchar(40)
);

CREATE TABLE IF NOT EXISTS Cliente(
    Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome varchar(40),
    Endereco varchar(60),
    Cidade varchar(20),
    Estado varchar(15),
    Telefone INTEGER,
    Documento INTEGER,
    email varchar(50)
);

CREATE TABLE IF NOT EXISTS Especie(
    Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome varchar(15)
);

CREATE TABLE IF NOT EXISTS Raca(
    Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    Descricao varchar(30)
);

CREATE TABLE IF NOT EXISTS Animal(
    Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome varchar(40),
    Dono integer NOT NULL,
    DataNascimento date,
    Especie INTEGER NOT NULL,
    Raca INTEGER NOT NULL,
    Sexo char(1),
    Cor varchar(10),
    FOREIGN KEY (Dono) REFERENCES Cliente(Codigo),
    FOREIGN KEY (Especie) REFERENCES Especie(Codigo),
    FOREIGN KEY (Raca) REFERENCES Raca(Codigo)
);

CREATE TABLE IF NOT EXISTS Pagamento(
    Tipo varchar(25) PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS CategoriaDeProduto(
    Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome varchar(30)
);

CREATE TABLE IF NOT EXISTS Produto(
    Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    Descricao varchar(50),
    Fabricante varchar(50),
    Categoria INTEGER,
    preco float,
    FOREIGN KEY (Categoria) REFERENCES CategoriaDeProduto(Codigo)
);

CREATE TABLE IF NOT EXISTS Servicos(
    Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    Descricao varchar(60),
    Preco float
);

CREATE TABLE IF NOT EXISTS Consulta(
    IDConsulta INTEGER PRIMARY KEY AUTOINCREMENT,
    DataConsulta date,
    Dono INTEGER NOT NULL,
    Animal INTEGER NOT NULL,
    Veterinario INTEGER,
    Pagamento varchar(25) NOT NULL,
    Servicos INTEGER,
    FOREIGN KEY (Dono) REFERENCES Cliente(Codigo),
    FOREIGN KEY (Animal) REFERENCES Animal(Codigo),
    FOREIGN KEY (Veterinario) REFERENCES Veterinario(Codigo),
    FOREIGN KEY (Pagamento) REFERENCES Pagamento(Tipo),
    FOREIGN KEY (Servicos) REFERENCES Servicos(Codigo)
);

CREATE TABLE IF NOT EXISTS Consulta_Medicamentos(
    IDConsulta INTEGER,
    IDProduto INTEGER,
    FOREIGN KEY (IDConsulta) REFERENCES Consulta(IDConsulta),
    FOREIGN KEY (IDProduto) REFERENCES Produto(Codigo),
    CONSTRAINT Consulta_Medicamentos PRIMARY KEY (IDConsulta, IDProduto)
);

CREATE TABLE IF NOT EXISTS CarrinhoDeProdutos(
    IDCarrinho INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE IF NOT EXISTS Carrinho_Produtos(
    IDCarrinho INTEGER,
    IDProduto INTEGER,
    FOREIGN KEY (IDCarrinho) REFERENCES CarrinhoDeProdutos(IDCarrinho),
    FOREIGN KEY (IDProduto)  REFERENCES Produto(Codigo),
    CONSTRAINT Carrinho_Produtos PRIMARY KEY (IDCarrinho, IDProduto)
);

CREATE TABLE IF NOT EXISTS Venda(
    IDVenda INTEGER PRIMARY KEY AUTOINCREMENT,
    Cliente INTEGER,
    DataVenda date,
    CarrinhoDeProdutos INTEGER,
    Pagamento varchar(25),
    Preco float,
    FOREIGN KEY (Cliente) REFERENCES Cliente(Codigo),
    FOREIGN KEY (CarrinhoDeProdutos) REFERENCES Carrinho_Produtos(IDCarrinho),
    FOREIGN KEY (Pagamento) REFERENCES Pagamento(Tipo)
);

CREATE TABLE IF NOT EXISTS Relatorio(
    Tipo varchar(255),
    IDRelatorio INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE IF NOT EXISTS Relatorio_Geral(
    IDRelatorio INTEGER,
    IDTipo INTEGER,
    FOREIGN KEY (IDRelatorio) REFERENCES Relatorio(Relatorio)
    CONSTRAINT Relatorio_Geral PRIMARY KEY (IDRelatorio, IDTipo)
);
