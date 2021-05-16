CREATE TABLE IF NOT EXISTS Veterinario(
    Codigo UUID PRIMARY KEY,
    Nome varchar(40),
    Endereco varchar(60),
    Cidade varchar(20),
    Estado varchar(15),
    FoneResidencia varchar(30),
    FoneCelular varchar(30)
);
CREATE TABLE IF NOT EXISTS Atendente(
    Codigo UUID PRIMARY KEY,
    Nome varchar(40)
);

CREATE TABLE IF NOT EXISTS Administrador(
    Codigo UUID PRIMARY KEY,
    Nome varchar(40)
);

CREATE TABLE IF NOT EXISTS Cliente(
    Codigo UUID PRIMARY KEY,
    Nome varchar(40),
    Endereco varchar(60),
    Cidade varchar(20),
    Estado varchar(15),
    Telefone INTEGER,
    Documento INTEGER,
    email varchar(50)
);

CREATE TABLE IF NOT EXISTS Especie(
    Codigo UUID PRIMARY KEY,
    Nome varchar(15)
);

CREATE TABLE IF NOT EXISTS Raca(
    Codigo UUID PRIMARY KEY,
    Descricao varchar(30)
);

CREATE TABLE IF NOT EXISTS Animal(
    Codigo UUID PRIMARY KEY,
    Nome varchar(40),
    Dono UUID NOT NULL,
    DataNascimento date,
    Especie UUID NOT NULL,
    Raca UUID NOT NULL,
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
    Codigo UUID PRIMARY KEY,
    Nome varchar(30)
);

CREATE TABLE IF NOT EXISTS Produto(
    Codigo UUID PRIMARY KEY,
    Descricao varchar(50),
    Fabricante varchar(50),
    Categoria UUID,
    Preco float,
    FOREIGN KEY (Categoria) REFERENCES CategoriaDeProduto(Codigo)
);

CREATE TABLE IF NOT EXISTS Servicos(
    Codigo UUID PRIMARY KEY,
    Descricao varchar(60),
    Preco float
);

CREATE TABLE IF NOT EXISTS Consulta(
    IDConsulta UUID PRIMARY KEY,
    DataConsulta date,
    Dono UUID NOT NULL,
    Animal UUID NOT NULL,
    Veterinario UUID,
    Pagamento varchar(25) NOT NULL,
    Servicos UUID,
    FOREIGN KEY (Dono) REFERENCES Cliente(Codigo),
    FOREIGN KEY (Animal) REFERENCES Animal(Codigo),
    FOREIGN KEY (Veterinario) REFERENCES Veterinario(Codigo),
    FOREIGN KEY (Pagamento) REFERENCES Pagamento(Tipo),
    FOREIGN KEY (Servicos) REFERENCES Servicos(Codigo)
);

CREATE TABLE IF NOT EXISTS Consulta_Medicamentos(
    IDConsulta UUID,
    IDProduto UUID,
    Quanditade integer,
    FOREIGN KEY (IDConsulta) REFERENCES Consulta(IDConsulta),
    FOREIGN KEY (IDProduto) REFERENCES Produto(Codigo),
    CONSTRAINT Consulta_Medicamentos PRIMARY KEY (IDConsulta, IDProduto)
);

CREATE TABLE IF NOT EXISTS CarrinhoDeProdutos(
    IDCarrinho UUID PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Carrinho_Produtos(
    IDCarrinho UUID,
    IDProduto UUID,
    FOREIGN KEY (IDCarrinho) REFERENCES CarrinhoDeProdutos(IDCarrinho),
    FOREIGN KEY (IDProduto)  REFERENCES Produto(Codigo),
    CONSTRAINT Carrinho_Produtos PRIMARY KEY (IDCarrinho, IDProduto)
);

CREATE TABLE IF NOT EXISTS Venda(
    IDVenda UUID PRIMARY KEY,
    Cliente UUID,
    DataVenda date,
    CarrinhoDeProdutos UUID,
    Pagamento varchar(25),
    Preco float,
    FOREIGN KEY (Cliente) REFERENCES Cliente(Codigo),
    FOREIGN KEY (CarrinhoDeProdutos) REFERENCES Carrinho_Produtos(IDCarrinho),
    FOREIGN KEY (Pagamento) REFERENCES Pagamento(Tipo)
);

CREATE TABLE IF NOT EXISTS Relatorio(
    Tipo varchar(255),
    IDRelatorio UUID PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Relatorio_Geral(
    IDRelatorio UUID,
    IDTipo UUID,
    FOREIGN KEY (IDRelatorio) REFERENCES Relatorio(Relatorio)
    CONSTRAINT Relatorio_Geral PRIMARY KEY (IDRelatorio, IDTipo)
);
