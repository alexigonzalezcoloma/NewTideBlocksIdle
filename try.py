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
        
        layout = GridLayout(cols=5, row_force_default=True, row_default_height=40, padding=[50,50,50,50])

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

        layout.add_widget(icon)
        layout.add_widget(btnfile)
        layout.add_widget(btnconex)
        layout.add_widget(btncomp)
        layout.add_widget(btnsend)

        return layout
    
if __name__=="__main__": IDLE().run()
