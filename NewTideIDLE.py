import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        parent= Widget()
        btnstart=Button(text='Inicio')
        btnconnect=Button(text='Conectar/Desconectar')
        parent.add_widget(btnconnect)
        parent.add_widget(btnstart)
        return parent

if __name__== '__main__':
    MyApp().run()
