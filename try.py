import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

from kivy.app import App

class IDLE(App):
    def build(self):
        mainlo = GridLayout(rows=2)
        
        optionslo = GridLayout(cols=5, row_force_default=True, row_default_height=40, padding=[50,50,50,50])

        icon = Button()
        icon.text = "NewTideIDLE"
        icon.background_color = [0.2, 0.2, 0.23, 1]
        
        btnfile = Button()
        btnfile.text = "Archivo"
        
        btnconex = Button()
        btnconex.text = "Conectar"

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
