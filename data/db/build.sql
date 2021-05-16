CREATE TABLE IF NOT EXISTS Veterinario(
    Codigo int PRIMARY KEY,
    Nome varchar(40),
    Endereco varchar(60),
    Cidade varchar(20),
    Estado varchar(15),
    FoneResidencia varchar(30),
    FoneCelular varchar(30)
);

CREATE TABLE IF NOT EXISTS Atendente(
    Codigo int PRIMARY KEY,
    Nome varchar(40)
);

CREATE TABLE IF NOT EXISTS Administrador(
    Codigo int PRIMARY KEY,
    Nome varchar(40)
);

CREATE TABLE IF NOT EXISTS Cliente(
    Codigo int PRIMARY KEY,
    Nome varchar(40),
    Endereco varchar(60),
    Cidade varchar(20),
    Estado varchar(15),
    Telefone int,
    Documento int,
    email varchar(50)
);

CREATE TABLE IF NOT EXISTS Especie(
    Codigo int PRIMARY KEY,
    Nome varchar(15)
);

CREATE TABLE IF NOT EXISTS Raca(h
    Codigo int PRIMARY KEY,
    Descricao varchar(30)
);

CREATE TABLE IF NOT EXISTS Animal(
    Codigo int,
    Nome varchar(40),
    Dono integer NOT NULL,
    DataNascimento date,
    Especie int NOT NULL,
    Raca int NOT NULL,
    Sexo char(1),
    Cor varchar(10),
    FOREIGN KEY (Dono) REFERENCES Cliente(Codigo),
    FOREIGN KEY (Especie) REFERENCES Especie(Codigo),
    FOREIGN KEY (Raca) REFERENCES Raca(Codigo),
    CONSTRAINT Animal PRIMARY KEY (Codigo, Dono)
);

CREATE TABLE IF NOT EXISTS Pagamento(
    Tipo varchar(25) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS CategoriaDeProduto(
    Codigo int PRIMARY KEY,
    Nome varchar(30)
);

CREATE TABLE IF NOT EXISTS Produto(
    Codigo int PRIMARY KEY,
    Descricao varchar(50),
    Fabricante varchar(50),
    Categoria int,
    preco float,
    FOREIGN KEY (Categoria) REFERENCES CategoriaDeProduto(Codigo)
);

CREATE TABLE IF NOT EXISTS Servicos(
    Codigo int PRIMARY KEY,
    Descricao varchar(60),
    Preco float
);

CREATE TABLE IF NOT EXISTS Consulta(
    IDConsulta int PRIMARY KEY,
    DataConsulta date,
    Dono int NOT NULL,
    Animal int NOT NULL,
    Veterinario int,
    Pagamento varchar(25) NOT NULL,
    Servicos int,
    FOREIGN KEY (Dono) REFERENCES Cliente(Codigo),
    FOREIGN KEY (Animal) REFERENCES Animal(Codigo),
    FOREIGN KEY (Veterinario) REFERENCES Veterinario(Codigo),
    FOREIGN KEY (Pagamento) REFERENCES Pagamento(Tipo),
    FOREIGN KEY (Servicos) REFERENCES Servicos(Codigo)
);

CREATE TABLE IF NOT EXISTS Consulta_Medicamentos(
    IDConsulta int,
    IDProduto int,
    FOREIGN KEY (IDConsulta) REFERENCES Consulta(IDConsulta),
    FOREIGN KEY (IDProduto) REFERENCES Produto(Codigo),
    CONSTRAINT Consulta_Medicamentos PRIMARY KEY (IDConsulta, IDProduto)
);

CREATE TABLE IF NOT EXISTS CarrinhoDeProdutos(
    IDCarrinho int PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Carrinho_Produtos(
    IDCarrinho int,
    IDProduto int,
    FOREIGN KEY (IDCarrinho) REFERENCES CarrinhoDeProdutos(IDCarrinho),
    FOREIGN KEY (IDProduto)  REFERENCES Produto(Codigo),
    CONSTRAINT Carrinho_Produtos PRIMARY KEY (IDCarrinho, IDProduto)
);

CREATE TABLE IF NOT EXISTS Venda(
    IDVenda int PRIMARY KEY,
    Cliente int,
    DataVenda date,
    CarrinhoDeProdutos int,
    Pagamento varchar(25),
    Preco float,
    FOREIGN KEY (Cliente) REFERENCES Cliente(Codigo),
    FOREIGN KEY (CarrinhoDeProdutos) REFERENCES Carrinho_Produtos(IDCarrinho),
    FOREIGN KEY (Pagamento) REFERENCES Pagamento(Tipo)
);

CREATE TABLE IF NOT EXISTS Relatorio(
    Tipo varchar(255),
    IDRelatorio int PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Relatorio_Geral(
    IDRelatorio int,
    IDTipo int,
    FOREIGN KEY (IDRelatorio) REFERENCES Relatorio(Relatorio)
    CONSTRAINT Relatorio_Geral PRIMARY KEY (IDRelatorio, IDTipo)
);
