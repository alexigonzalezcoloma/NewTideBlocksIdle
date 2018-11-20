class Bloque():

    def __init__(self):
        self.outs = None
        self.ant = None

    def write(self):
        raise Exception("No funciona :v")

    def add_ins(self, nodo):
        self.ins = nodo

    def add_outs(self, nodo):
        self.outs = nodo
        self.outs.ant = self
