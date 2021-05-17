from src.dao.DAO import DAO
from src.db import db
from src.sys.pagamento import Pagamento

class PagamentoDAO(DAO):

    def __parseDataToObject(self, data):
        return Pagamento(
            data[0]
        )

    def __init__(self):
        super().__init__('Pagamento', 'Tipo')
    
    def add(self, Pagamento):
        lista  = Pagamento.read()
        t = db.execute(f'INSERT INTO Pagamento VALUES (?)', lista)
        db.commit()
        return t

    def getByType(self, Tipo):
        pagamento = super().getByID(Tipo)
        if not pagamento:
            return None
        return self.__parseDataToObject(pagamento)

    def getAll(self):
        pagamentos = super().getAll()
        parsedPagamento = []
        for pagamento in pagamentos:
            parsedPagamento.append(self.__parseDataToObject(pagamento))
        return parsedPagamento