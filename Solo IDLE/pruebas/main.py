import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder
from kivy.uix.button import Button


def FileDialog(instance):
    content = BoxLayout(orientation='vertical', spacing=5)
    popup = Popup(title='Choose a file', content=content, size_hint=(None, None),size=(400, 400))

    path = os.getcwd()
    textinput = FileChooserListView(path=path, size_hint=(1, 1), dirselect=True)

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
    ports = list(serial.tools.list_ports.comports())
    content = BoxLayout(orientation='vertical', spacing=5)
    btnclose = Button(text='Close')
    content.add_widget(btnclose)
    popup = Popup(title='Choose a port', content=content, auto_dismiss=False, size_hint=(None, None),
                  size=(400, 400))
    btnclose.bind(on_press=popup.dismiss)
    popup.open()


class IDLE(BoxLayout):
	None
	
class MainApp(App):
	title = "NEWTIDEIDLE"
	def build(self):
		return IDLE()
		
if __name__ == "__main__":
	MainApp().run()