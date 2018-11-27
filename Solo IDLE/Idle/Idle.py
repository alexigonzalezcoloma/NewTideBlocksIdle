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

import os, serial

def validate(instance):
    print("funciona")

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
    ports = list(serial.tools.list_ports.comports())
    content = BoxLayout(orientation='vertical', spacing=5)
    btnclose = Button(text='Close')
    content.add_widget(btnclose)
    popup = Popup(title='Choose a port', content=content, auto_dismiss=False, size_hint=(None, None),
                  size=(400, 400))
    btnclose.bind(on_press=popup.dismiss)
    popup.open()

# Define la clase de la aplicacion
class IDLE(App):
    Window.clearcolor = (1, 1, 1, 1)
    Config.set('graphics', 'minimum_width', '720')
    Config.set('graphics', 'minimum_height', '640')
    def build(self):
        mainlo = GridLayout(rows=2, cols=1)

        optionslo = GridLayout(cols=5, size_hint=(0.1,0.2), row_force_default=True, row_default_height=40, padding=[50,50,50,50])

        icon = Button()
        icon.text = "NewTideIDLE"
        icon.background_color = [0, 0, 0, 1]

        btnfile = Button()
        btnfile.text = "Archivo"
        btnfile.bind(on_press=FileDialog)

        btnconex = Button()
        btnconex.text = "Conectar"
        btnconex.bind(on_press=ConnectionDialog)

        btncomp = Button()
        btncomp.text = "Compilar"
        btncomp.background_color = [0, 0, 0, 1]

        btnsend = Button()
        btnsend.text = "Enviar"

        optionslo.add_widget(icon)
        optionslo.add_widget(btnfile)
        optionslo.add_widget(btnconex)
        optionslo.add_widget(btncomp)
        optionslo.add_widget(btnsend)

        parealo = GridLayout(cols=2, padding=[10,10])
        blockslo = GridLayout(rows=2)
        blocksopslo = GridLayout(cols=3 ,size_hint=(0.1,0.1))
        blocksarealo = GridLayout(cols=1,rows=1)
        codearealo = GridLayout(cols=1)



        btnq4=Button()
        btnq5=Button()

        blocksarealo.add_widget(btnq4)
        codearealo.add_widget(btnq5)

        btnbmaker = Button()
        btnbmaker.text = "Maker"

        btnbcontrol = Button()
        btnbcontrol.text = "Control"

        btnboperators = Button()
        btnboperators.text = "Operadores"

        blocksopslo.add_widget(btnbmaker);blocksopslo.add_widget(btnbcontrol);blocksopslo.add_widget(btnboperators);
        #area = BoxLayout(height='50dp')
        #blocksarealo.add_widget(area)

        #area2 = BoxLayout(height='50dp')
        #codearealo.add_widget(area2)

        blockslo.add_widget(blocksopslo)
        blockslo.add_widget(blocksarealo)

        parealo.add_widget(blockslo);parealo.add_widget(codearealo)



        mainlo.add_widget(optionslo)
        mainlo.add_widget(parealo)
        return mainlo



if __name__=="__main__": IDLE().run()

