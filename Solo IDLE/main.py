import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Color
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.config import Config
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.scatter import Scatter
import os

class IDLE(BoxLayout):


        def validate(instance):
                print("funciona")

        # Muestra alertas luego de compilar o enviar
	def Alert(ins, res):
                content = BoxLayout(orientation='vertical', spacing=5)
                popup = Popup(title='Alerta', content=content, auto_dismiss=False, size_hint=(None, None), size=(480, 160))
    
                txt = Label(text='Ha ocurrido un error') 
                if ins == 1:
                        if res:
                                txt = Label(text='Se ha compilado correctamente')
                if ins == 2:
                        if res:
                                txt = Label(text='Se ha cargado el hardware')

                content.add_widget(txt)
                btnlayout = BoxLayout(size_hint_y=None, height='50dp', spacing='5dp')
                btn = Button(text='Aceptar')
                btn.bind(on_release=popup.dismiss)
                btnlayout.add_widget(btn)
                content.add_widget(btnlayout)
    
                popup.open()

        # Invocación de compilador de arduino
        def Compilate(instance):
                nfh = open("Compilador/Builder/temp/temp/temp.ino", "a")
                nfh.write("}")
                nfh.close()
                dp = Compilador.Compilador("Windows").dump_prefs()
                if dp == 0:
                        cp = Compilador.Compilador("Windows").compilate()
                        if cp == 0:
                                return Alert(1, 1)
                return Alert(1, 0)

        # Envia .hex a hardware
        def Send(instance):
                resp = Compilador.Compilador("Windows").send("COM3")
                param = 0
                if resp == 0:
                        param = 1
                return Alert(2, param)

        # Copia archivo base a archivo temporal para la compilación
        def FileBase():
                nfh = open("Compilador/Builder/temp/temp/temp.ino", "w")
                with open("Compilador/Builder/temp/base/base.ino") as f:
                        content = f.readlines()
                for line in content:
                        nfh.write(line)
                f.close()
                nfh.close()


        # Abre popup con directorio de archivos
        def FileDialog(instance):
                content = BoxLayout(orientation='vertical', spacing=5)
                popup = Popup(title='Choose a file', content=content, size_hint=(None, None),size=(400, 400))

                path = os.getcwd()
                textinput = FileChooserListView(path=path, size_hint=(1, 1), dirselect=True)
                #textinput.bind(on_path=validate)
                #textinput = textinput

                content.add_widget(textinput)

                btnlayout = BoxLayout(size_hint_y=None, height='50dp', spacing='5dp')
                btn = Button(text='Ok')
                btn.bind(on_release=validate)
                btnlayout.add_widget(btn)
                btn = Button(text='Cancel')
                btn.bind(on_release=popup.dismiss)
                btnlayout.add_widget(btn)
                content.add_widget(btnlayout)
                popup.open()


        # Abre popup para selección de puerto serial
        def ConnectionDialog(instance):
                print(list(serial.tools.list_ports.comports()))
                content = BoxLayout(orientation='vertical', spacing=5)
                btnclose = Button(text='Close')
                content.add_widget(btnclose)
                popup = Popup(title='Choose a port', content=content, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
                btnclose.bind(on_press=popup.dismiss)
                popup.open()

                
	def function_drags(self):
		#scatter = Scatter(do_rotation=False)
		#scatter.add_widget(subtraction)
		print('hola')
	
	def modmakers(self):
		areamodules=self.ids.areamodules
		areamodules.clear_widgets()

		led_on=Button(text='Encender Led')
		led_on.bind(fxled_on('13'))
		led_off=Button(text='Apagar Led')
		poweron_pin=Button(text='Encender Pin')
		poweroff_pin=Button(text='Apagar pin')
		read_analog_pin=Button(text='Leer Pin')

		areamodules.add_widget(led_on)
		areamodules.add_widget(led_off)
		areamodules.add_widget(poweron_pin)
		areamodules.add_widget(poweroff_pin)
		areamodules.add_widget(read_analog_pin)

	def modcontrols(self):
		areamodules=self.ids.areamodules
		areamodules.clear_widgets()

		control_if=Button(text='If(Condicion)')
		control_time=Button(text='Pause(time)')
		control_while=Button(text='While(Condicion)')

		areamodules.add_widget(control_if)
		areamodules.add_widget(control_time)
		areamodules.add_widget(control_while)


	def modopr(self):
		
		areamodules=self.ids.areamodules
		areamodules.clear_widgets()
		mod_sum=Button(text='()+()')
		mod_sum.Color=(0,1,1)
		subtraction=Button(text='()-()')
		multiplication=Button(text='()x()')
		division=Button(text='()/()')
		greater_than=Button(text='()>()')
		smaller_than=Button(text='()<()')
		same_that=Button(text='()==()')

		areamodules.add_widget(mod_sum)
		areamodules.add_widget(subtraction)
		areamodules.add_widget(division)
		areamodules.add_widget(greater_than)
		areamodules.add_widget(smaller_than)
		areamodules.add_widget(same_that)

	def fxled_on(self,n):
	    #nfh = open("Compilador/temp/temp.ino", "a")
	    x = Modulo.Led_On(n)
	    x.write(0, "")
	    #nfh.write(x.write(0, ""))


class MainApp(App):
	title = "NEWTIDEIDLE"
	def build(self):
		self.IDLE=IDLE()
		return self.IDLE
		
if __name__ == "__main__":
	MainApp().run()
