from uuid import uuid4

class Relatorio:

    def __init__(self, tipo, IDRelatorio = None):
        if not IDRelatorio:
            IDRelatorio = str(uuid4())
        self.tipo = tipo
        self.IDRelatorio = lista

    def read(self):
        return (self.tipo, self.lista)