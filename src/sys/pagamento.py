class Pagamento:

    def __init__(self, tipo):
        self.__tipo = tipo

    def read(self):
        return (self.__tipo,)