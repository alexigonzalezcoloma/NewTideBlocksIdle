from bloques import Bloque

class Delay(Bloque):

    def __init__(self, t):
        Bloque.__init__(self)
        self.name = "while"
        self.t = t
        self.ins = None

    def write(self, tabs, code):
        code += "    " * tabs
        code += "delay(%s);\n" % (self.t)
        if self.outs:
            code = self.outs.write(tabs, code)
        return code