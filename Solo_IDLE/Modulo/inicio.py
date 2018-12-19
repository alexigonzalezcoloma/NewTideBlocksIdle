from bloques import Bloque

class Inicio(Bloque):

    def __init__(self):
        Bloque.__init__(self)
        self.name = "inicio"
        self.ins = None

    def write(self, tabs, code):
        code += "    " * tabs
        code += "\n"
        if self.ins:
            code = self.ins.write(tabs+1, code)
        if self.outs:
            code = self.outs.write(tabs, code)
        return code