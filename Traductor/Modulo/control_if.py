from bloques import Bloque

class If(Bloque):

    def __init__(self, cond):
        Bloque.__init__(self)
        self.name = "if"
        self.cond = cond
        self.ins = None

    def write(self, tabs, code):
        code += "    " * tabs
        code += "if (%s){\n" % (self.cond)
        if self.ins:
            code = self.ins.write(tabs+1, code)
        code += "    " * tabs
        code += "}\n"
        if self.outs:
            code = self.outs.write(tabs, code)
        return code

if __name__ == '__main__':
    x = If("a>1")
    x.ins = If("asd = jajachupalo")
    x.ins.ins = If("asd")
    print (x.write(0, ""))
