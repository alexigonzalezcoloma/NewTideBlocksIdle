import Modulo
import Modulo.__init__


if __name__ == '__main__':
    x = If("a > b")
    x.outs = Else()
    x.outs.ant = x
    x.outs.ins = If("asd")
    print (x.write(0,""))