import sys; sys.path.insert(0, 'Modulo'); import Modulo; import Idle


if __name__ == '__main__':
    inicio = Modulo.While("True"); nodo = inicio
    nodo.add_ins(Modulo.If('"condición 2"'))
    nodo = nodo.ins; asd = nodo
    nodo.add_ins(Modulo.Led_On("13"))
    nodo = nodo.ins
    nodo.add_outs(Modulo.Delay("1000"))
    nodo = asd
    nodo.add_outs(Modulo.Else())
    nodo.outs.ant = nodo; nodo = nodo.outs
    nodo.add_ins(Modulo.Led_Off("13"))
    

    print (inicio.write(0,""))