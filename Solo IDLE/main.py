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

Config.set("graphics", "height",720)
Config.set("graphics", "width",1280)

class Idle(BoxLayout):
	pass

class MainApp(App):
	title ="NewTIDEIDLE"
	def build(self):
		return Idle()

if __name__ == '__main__':
	MainApp().run() 
