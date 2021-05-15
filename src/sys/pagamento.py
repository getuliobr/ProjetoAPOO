class Pagamento:

    def __init__(self, tipo):
        self.tipo = tipo
    
    def update(self, tipo= False):
        if(tipo):
            self.tipo = tipo