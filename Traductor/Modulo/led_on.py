from bloques import Bloque

class Led_On(Bloque):

    def __init__(self, color):
        Bloque.__init__(self)
        self.name = "ledon"
        self.color = color
        self.ins = None

    def write(self, tabs, code):
        code += "    " * tabs
        code += "digitalWrite(%s, HIGH);\n" % (self.color)
        if self.outs:
            code = self.outs.write(tabs, code)
        return code
        