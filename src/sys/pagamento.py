class Pagamento:

    def __init__(self, tipo):
        self.tipo = tipo

    def read(self):
        return (self.tipo,)