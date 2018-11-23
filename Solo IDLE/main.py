import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.uix.image import Image
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
		print(self.ids.areamodules)
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

	

	
	
class MainApp(App):
	title = "NEWTIDEIDLE"
	def build(self):
		self.IDLE=IDLE()
		return self.IDLE
		
if __name__ == "__main__":
	MainApp().run()