import serial

ser = serial.Serial("COM3", 9600)
print ("Introduce un caracter ('s' para salir): "); entrada = " "

while entrada != 's': #introduciendo 's' salimos del bucle
   entrada = str(input()) #introduce otro caracter por teclado
   ser.write(str.encode(entrada)) #envia la entrada por serial
ser.close()