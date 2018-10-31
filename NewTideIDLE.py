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

        btnfile = Button()
        btnfile.text = "Archivo"
        btnfile.pos = (170,560)
        btnfile.size = (100, 30)

        btnconex = Button()
        btnconex.text = "Conectar"
        btnconex.pos = (300,560)
        btnconex.size = (100, 30)

        btncomp = Button()
        btncomp.text = "Compilar"
        btncomp.pos = (430,560)
        btncomp.size = (100, 30)

        btnsend = Button()
        btnsend.text = "Enviar"
        btnsend.pos = (620,560)
        btnsend.size = (100, 30)
        
        
        wdg.add_widget(btnfile)
        wdg.add_widget(btnconex)
        wdg.add_widget(btncomp)
        wdg.add_widget(btnsend)

        '''
        btnmod= Button()
        btnmod.text = "Control/maker/Operdores"
        btnmod.pos = (0,0)
        btnmod.size = (200, 500)

        btncod= Button()
        btncod.text = "Arrastre aqui los modulos seleccionados"
        btncod.pos = (300,0)
        btncod.size = (450, 500)

        wdg.add_widget(btnmod)
        wdg.add_widget(btncod)
        '''
        
        lbl.markup= True
        lbl.pos = (300,300)
        lbl.font_size = "24dp"
        lbl.color = [1, 0.5,0.5,1]
        wdg.add_widget(lbl)
        return wdg

    


if __name__=="__main__": Boton().run()
