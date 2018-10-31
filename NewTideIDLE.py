import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

class Boton(App):
    def build(self):
        global wdg
        global lbl
        global btn
        wdg = Widget()
        lbl = Label()
        btn = Button()
        btn.text = "Archivo"
        btn.pos = (170,560)
        btn.size = (100, 30)
        wdg.add_widget(btn)
        lbl.markup= True
        lbl.pos = (300,300)
        lbl.font_size = "24dp"
        lbl.color = [1, 0.5,0.5,1]
        wdg.add_widget(lbl)
        return wdg

    


if __name__=="__main__": Boton().run()
