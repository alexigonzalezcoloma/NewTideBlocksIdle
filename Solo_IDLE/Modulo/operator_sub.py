from bloques import Bloque

class Subtraction(Bloque):

    def __init__(self, val1, val2):
        Bloque.__init__(self)
        self.name = "sub"
        self.val1 = val1
        self.val2 = val2
        self.ins = None

    def write(self, tabs, code):
        code += "    " * tabs
        code += "%s - %s" % (self.val1, self.val2)
        return code
