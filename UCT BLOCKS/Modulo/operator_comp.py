from bloques import Bloque

class Comparison(Bloque):

    def __init__(self, cond, val1, val2):
        Bloque.__init__(self)
        self.name = "sub"
        self.cond = cond
        self.val1 = val1
        self.val2 = val2
        self.ins = None

    def write(self, tabs, code):
        code += "    " * tabs
        code += "%s %s %s" % (self.val1, self.cond, self.val2)
        return code
