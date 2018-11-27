import serial
from bloques import Bloque

class connect(Bloque):
	def __init__(self, arg):
		Bloque.__init__(self)
		self.name = "connect"
		self.ins = None		

		def conn():
			try:
				conn = serial.Serial("COM4", 9600)
				print("Conectado a Tide Makers Mini")
			except Exception as e:
				raise("Tarjeta no conectada ya que no hay un puerto disponible")

		def dis():
			try:
				conn.close()
				print("Desconectado")
			except Exception as e:
				raise("Error al desconectar")

