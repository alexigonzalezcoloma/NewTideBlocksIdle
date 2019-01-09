from bloques import Bloque

class Else(Bloque):

    def __init__(self):
        Bloque.__init__(self)
        self.name = "else"
        self.ins = None

    def write(self, tabs, code):
        if self.ant:
            if self.ant.name == "if":  
                code += "    " * tabs
                code += "else{\n"
                if self.ins:
                    code = self.ins.write(tabs+1, code)
                code += "    " * tabs
                code += "}\n"
        return code



 