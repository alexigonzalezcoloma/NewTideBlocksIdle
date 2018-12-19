from bloques import Bloque

class While(Bloque):

    def __init__(self, cond):
        Bloque.__init__(self)
        self.name = "while"
        self.cond = cond
        self.ins = None

    def write(self, tabs, code):
        code += "    " * tabs
        code += "for i=0; i<=(%s); i++{\n" % (self.cond)
        if self.ins:
            code = self.ins.write(tabs+1, code)
        code += "    " * tabs
        code += "}\n"
        if self.outs:
            code = self.outs.write(tabs, code)
        return code
