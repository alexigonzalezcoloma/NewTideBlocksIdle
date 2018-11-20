import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Box01(BoxLayout):
	None
	
class MainApp(App):
	title = "NEWTIDEIDLE"
	def build(self):
		return Box01()
		
if __name__ == "__main__":
	MainApp().run()