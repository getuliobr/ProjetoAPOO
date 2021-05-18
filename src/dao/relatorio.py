from . import DAOCliente
from . import DAOProduto
from . import DAOConsulta
from . import DAOPagamento
from . import DAOVenda
from . import DAOClasses


class Relatorio:

    def __init__(self, tipo, id = None):
        self.tipo = tipo
        if id:
            self.id = id
        
        self.__ClienteDAO = DAOCliente.ClienteDAO()
        self.__AnimalDAO = DAOCliente.AnimalDAO(self.__ClienteDAO, DAOCliente.EspecieDAO(), DAOCliente.RacaDAO())
        self.__ProdutoDAO = DAOProduto.ProdutoDAO(DAOProduto.CategoriaDeProdutoDAO())
        self.__VeterinarioDAO = DAOClasses.VeterinarioDAO()
        self.__PagamentoDAO = DAOPagamento.PagamentoDAO()
        self.__ServicoDAO = DAOConsulta.ServicoDAO()
        self.__ConsultaDAO = DAOConsulta.ConsultaDAO(self.__ClienteDAO,self.__AnimalDAO,self.__ProdutoDAO,self.__VeterinarioDAO,self.__PagamentoDAO, self.__ServicoDAO)

    def printRelatorio(self):
        if self.tipo == 'Animais':
            lista = self.__AnimalDAO.getAll()
            print(
                "{:40} {:15} {:30} {:20} {:10} {:10} {:10} {:10}"
                .format('Codigo', 'Nome', 'Dono', 'Data de Nascimento', 'Especie', 'Raça', 'Sexo', 'Cor')
            )
            for animais in lista:
                animal = list(animais.read())
                print(
                    "{:40} {:15} {:30} {:20} {:10} {:10} {:10} {:10}"
                    .format(animal[0], animal[1], animal[2].read()[1], animal[3], animal[4].read()[1], animal[5].read()[1], animal[6], animal[7])
                )
            
        if self.tipo == 'Produtos':
            lista = self.__ProdutoDAO.getAll()
            print(
                "{:40} {:30} {:30} {:15} {:10}"
                .format('Codigo','Descrição','Fabricante','Categoria','Preço')
            )
            for produtos in lista:
                produto = list(produtos.read())
                print(
                    "{:40} {:30} {:30} {:15} {:10}"
                    .format(produto[0],produto[1], produto[2], produto[3].read()[1], produto[4])
                )

        # if self.tipo == 'Consultas':
        #     lista = self.__ConsultaDAO.getAll()
        #     print(lista[0].read)
            # print(
            #     "{:40} {:30} {:30} {:15} {:10} {:10} {:10} {:10}"
            #     .format('Codigo','Data','Dono','Animal','Veterinario','Pagamento','Servicos','Valor')
            # )
            # for consultas in lista:
            #     consulta = list(consultas.read())
            #     preco = consulta[6].read()[2]
            #     for medicamento in consulta
        
        # if self.tipo == 'Faturamento':

