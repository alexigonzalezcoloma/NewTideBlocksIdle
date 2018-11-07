from pyfirmata import Arduino, util
import time

#conexion con firmata
board= Arduino('COM3')
iterator = util.Iterator(board);iterator.start()

#variables y pines
entrada=" "
V =board.get_pin("a:0:i")
#B =board.get_pin("d:3:p")
namepin = [{"pin":"w", "n":13},
           {"pin":"r", "n":6},
           {"pin":"y", "n":5},
           {"pin":"g", "n":4},
           {"pin":"p", "n":3}]

#funcion map
def MAP(x,vi,vf,vis,vfs):
    return ((((x-vi)*(vfs-vis))/(vf-vi))+vis)

#funcion menu
def Pin(x):
    for i in range(len(namepin)):
        if x == namepin[i]["pin"]:
            if board.digital[namepin[i]["n"]].read()!=1:board.digital[namepin[i]["n"]].write(1)
            else:board.digital[namepin[i]["n"]].write(0)

    if x == "test":
        for i in range(len(namepin)):
            board.digital[namepin[i]["n"]].write(1)
            time.sleep(0.5)
        for i in range(len(namepin)):
            board.digital[namepin[i]["n"]].write(0)
            time.sleep(0.5)
        print ("test finalizado")

    if x == "l":
        asd = V.read()
        print (MAP(asd, 1, 0, 0, 100))


#main
while entrada != "s":
    entrada=str(input())
    Pin(entrada)
board.exit()