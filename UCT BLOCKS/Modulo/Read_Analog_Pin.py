from bloques import Bloque

class Read_Analog_Pin(Bloque):

    def __init__(self, pin):
        Bloque.__init__(self)
        self.name = "Read_Analog_Pin"
        self.pin = pin
        self.ins = None

    def write(self, tabs, code):
        code += "    " * tabs
        code += "analogRead(%s);\n" % (self.pin)
        if self.outs:
            code = self.outs.write(tabs, code)
        return code