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
from kivy.app import App

import os

def test(instance):
    # create popup layout
    content = BoxLayout(orientation='vertical', spacing=5)
    popup = Popup(title='Choose a file', content=content, size_hint=(None, None),size=(400, 400))
    '''
   # create the filechooser
    textinput = FileChooserListView(path=(os.path.join(path, filename[0])), size_hint=(1, 1), dirselect=True)
    textinput.bind(on_path=self._validate)
    textinput = textinput
 
    # construct the content
    content.add_widget(textinput)
    content.add_widget(SettingSpacer())
    
    # 2 buttons are created for accept or cancel the current value
    btnlayout = BoxLayout(size_hint_y=None, height='50dp', spacing='5dp')
    btn = Button(text='Ok')
    btn.bind(on_release=btn._validate)
    btnlayout.add_widget(btn)
    btn = Button(text='Cancel')
    btn.bind(on_release=btn._dismiss)
    btnlayout.add_widget(btn)
    content.add_widget(btnlayout)
    '''
 
    # all done, open the popup !
    popup.open()

def FileDialog(instance):
    content = Button(text='Close')
    popup = Popup(title='Choose a file', content=content, auto_dismiss=False, size_hint=(None, None),            
                  size=(400, 400))
    content.bind(on_press=popup.dismiss)
    popup.open()

def ConnectionDialog(instance):
    content = Button(text='Close')
    popup = Popup(title='Choose a port', content=content, auto_dismiss=False, size_hint=(None, None),            
                  size=(400, 400))
    content.bind(on_press=popup.dismiss)
    popup.open()

'''        
def FileDialog(BoxLayout):

    def open(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            print(f.read())

    def selected(self, filename):
        print("selected: %s" % filename[0])
'''

class IDLE(App):
    def build(self): 
        mainlo = GridLayout(rows=2)
        
        optionslo = GridLayout(cols=5, row_force_default=True, row_default_height=40, padding=[50,50,50,50])

        icon = Button()
        icon.text = "NewTideIDLE"
        icon.background_color = [0.2, 0.2, 0.23, 1]
        
        btnfile = Button()
        btnfile.text = "Archivo"
        btnfile.bind(on_press=FileDialog)
        
        btnconex = Button()
        btnconex.text = "Conectar"
        btnconex.bind(on_press=ConnectionDialog)

        btncomp = Button()
        btncomp.text = "Compilar"

        btnsend = Button()
        btnsend.text = "Enviar"

        optionslo.add_widget(icon)
        optionslo.add_widget(btnfile)
        optionslo.add_widget(btnconex)
        optionslo.add_widget(btncomp)
        optionslo.add_widget(btnsend)

        parealo = GridLayout(cols=2, padding=[10,10])
        
        blockslo = GridLayout(rows=2)
        blocksopslo = GridLayout(cols=3)
        blocksarealo = GridLayout(cols=1)
        codearealo = GridLayout(cols=1)

        btnbmaker = Button()
        btnbmaker.text = "Maker"
        
        btnbcontrol = Button()
        btnbcontrol.text = "Control"

        btnboperators = Button()
        btnboperators.text = "Operadores"

        blocksopslo.add_widget(btnbmaker);blocksopslo.add_widget(btnbcontrol);blocksopslo.add_widget(btnboperators);
        area = Image(); area.source="fondo.jpg"; area.size=(300,500)
        blocksarealo.add_widget(area)

        area2 = Image(); area2.source="fondo.jpg"; area2.size=(300,500)
        codearealo.add_widget(area2)
        
        blockslo.add_widget(blocksopslo)
        blockslo.add_widget(blocksarealo)
        
        parealo.add_widget(blockslo);parealo.add_widget(codearealo)

        mainlo.add_widget(optionslo)
        mainlo.add_widget(parealo)
        return mainlo
    
if __name__=="__main__": IDLE().run()
