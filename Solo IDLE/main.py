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
import os

class IDLE(BoxLayout):

	def FileDialog(self):
		content = BoxLayout(orientation='vertical', spacing=5)
		popup = Popup(title='Choose a file', content=content, size_hint=(None, None),size=(400, 400))

		path = os.getcwd()
		textinput = FileChooserListView(path=path, size_hint=(1, 1), dirselect=True)

		content.add_widget(textinput)

		btnlayout = BoxLayout(size_hint_y=None, height='50dp', spacing='5dp')
		btn = Button(text='Ok')
	   
		btnlayout.add_widget(btn)
		btn = Button(text='Cancel')
		btn.bind(on_release=popup.dismiss)
		btnlayout.add_widget(btn)
		content.add_widget(btnlayout)
		popup.open()
	
	def validate(instance):
		print("funciona")


	# Abre popup para selección de puerto serial
	def ConnectionDialog(instance):
		ports = list(serial.tools.list_ports.comports())
		content = BoxLayout(orientation='vertical', spacing=5)
		btnclose = Button(text='Close')
		content.add_widget(btnclose)
		popup = Popup(title='Choose a port', content=content, auto_dismiss=False, size_hint=(None, None),
					  size=(400, 400))
		btnclose.bind(on_press=popup.dismiss)
		popup.open()

	
	
	def modmakers(self):
		areamodules=self.ids.areamodules
		areamodules.clear_widgets()

		led_on=Button(text='Encender Led')
		led_on.Color=(1, 0, 0)
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


	
class MainApp(App):
	title = "NEWTIDEIDLE"
	def build(self):
		self.IDLE=IDLE()
		return self.IDLE
		
if __name__ == "__main__":
	MainApp().run()