import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Color
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.checkbox import CheckBox
from kivy.config import Config
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.scatter import Scatter
import os, sys; sys.path.insert(0, 'Modulo'); import Modulo;
from Compilador import Compilador

import serial.tools.list_ports

class IDLE(BoxLayout):

        def DynamicButton(self, instance):
                global xpos, ypos, nbtn

                programarea = self.ids.areamodulesprogram
                btext = instance.text
                bcolor = instance.background_color

                dbtn = "dbtn"+str(nbtn)

                self.dbtn = Button(text=btext, id=str(nbtn),
                              size_hint=(0.25,0.1), pos_hint={'x':xpos,'y':ypos},
                              background_color=bcolor)
                self.dbtn.bind(on_press=self.DynamicClear)

                if ypos > 0.15 and xpos < 1:
                        ypos -= 0.10
                        nbtn += 1; programarea.add_widget(self.dbtn)
                elif xpos < 1:
                        nbtn += 1; programarea.add_widget(self.dbtn)
                        xpos += 0.3
                        ypos = 0.85

        def DynamicClear(self, instance):
                programarea = self.ids.areamodulesprogram
                programarea.remove_widget(instance)
                

        def Alert(ins, res):
                content = BoxLayout(orientation='vertical', spacing=5)
                popup = Popup(title='Alerta', content=content, auto_dismiss=False, size_hint=(None, None), size=(480, 160))

                txt = Label(text='Ha ocurrido un error')
                if ins == 1:
                        if res:
                                txt = Label(text='Se ha compilado correctamente')
                if ins == 2:
                        if res:
                                txt = Label(text='Se ha cargado el hardware')
                if ins == 3:
                        if res:
                                txt = Label(text='Se ha seleccionado correctamente el puerto')

                content.add_widget(txt)
                btnlayout = BoxLayout(size_hint_y=None, height='50dp', spacing='5dp')
                btn = Button(text='Aceptar')
                btn.bind(on_release=popup.dismiss)
                btnlayout.add_widget(btn)
                content.add_widget(btnlayout)

                popup.open()


        # Invocación de compilador de arduino
        def Compilate(instance):
                nfh = open("Compilador/Builder/temp/temp/temp.ino", "a")
                nfh.write("}")
                nfh.close()
                dp = Compilador("Windows").dump_prefs()
                if dp == 0:
                        cp = Compilador("Windows").compilate()
                        if cp == 0:
                                return IDLE.Alert(1, 1)
                return IDLE.Alert(1, 0)

        # Envia .hex a hardware
        def Send(instance):
                param = 0
                
                try:
                        resp = Compilador("Windows").send(actualport)
                except NameError:
                        return IDLE.Alert(2, param)
                if resp == 0:
                        param = 1
                IDLE.FileBase() # Copia base a temp.ino
                return IDLE.Alert(2, param)

        # Copia archivo base a archivo temporal para la compilación
        def FileBase():
                nfh = open("Compilador/Builder/temp/temp/temp.ino", "w")
                with open("Compilador/Builder/temp/base/base.ino") as f:
                        content = f.readlines()
                for line in content:
                        nfh.write(line)
                f.close()
                nfh.close()

        def FileDialog(self):
                content = BoxLayout(orientation='vertical', spacing=5)
                popup = Popup(title='Choose a file', content=content, size_hint=(None, None),size=(400, 400))

                path = os.getcwd()
                textinput = FileChooserListView(path=path, size_hint=(1, 1), dirselect=True)

                content.add_widget(textinput)

                btnlayout = BoxLayout(size_hint_y=None, height='50dp', spacing='5dp')
                btn = Button(text='Ok')

                btnlayout.add_widget(btn)
                btn = Button(text='Cancel')
                btn.bind(on_release=popup.dismiss)
                btnlayout.add_widget(btn)
                content.add_widget(btnlayout)
                popup.open()

        def SavePort(instance):
                global actualport
                instance.active = True
                actualport = instance.text
                return IDLE.Alert(3,1)

        # Abre popup para selección de puerto serial
        def ConnectionDialog(instance):
                cbs = []
                ports = list(serial.tools.list_ports.comports())
                
                content = BoxLayout(orientation='vertical', spacing=5)
                lports = BoxLayout(orientation='vertical', spacing=1)

                try:
                        ap = ' -------------------------------- Currently using: '+actualport
                except NameError:
                        ap = ''
                popup = Popup(title='Choose a port'+ap, content=content, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
                
                i = 1
                if len(ports) >= 1:
                        for port in sorted(ports):
                                portname = port
                                cb = CheckBox(); cb.text = (str(portname)[:4]) ; cb.group = 'group'
                                cb.bind(on_press=IDLE.SavePort)
                                cbs.append(cb)
                                lbl = Label(); lbl.text = (str(portname)[:4])
                                lports.add_widget(cb); lports.add_widget(lbl)
                                i += 1
                else:
                        msg = "No hay puertos disponibles"
                        msglbl = Label(); msglbl.text = msg; lports.add_widget(msglbl)

                btnclose = Button(text='Close')
                btnclose.bind(on_press=popup.dismiss)
                
                content.add_widget(lports)
                content.add_widget(btnclose)
                
                popup.open()

        def function_drags(self):
                #scatter = Scatter(do_rotation=False)
                #scatter.add_widget(subtraction)
                print('hola')


        def modmakers(self):
                dropdownon = DropDown()
                Colors = ["Encender blanco","Encender rojo","Encender verde","Encender naranjo"]
                for index in range(4):
                    btnon = Button(text='%s' % Colors[index], size_hint_y=None, height=44)
                    btnon.bind(on_press=self.DynamicButton)
                    dropdownon.add_widget(btnon)

                dropdownoff = DropDown()
                Colors = ["Apagar blanco","Apagar rojo","Apagar verde","Apagar naranjo"]
                for index in range(4):
                    btnoff = Button(text='%s' % Colors[index], size_hint_y=None, height=44)
                    btnoff.bind(on_press=self.DynamicButton)
                    dropdownoff.add_widget(btnoff)

                dropdownpin=DropDown()
                pins = ["Leer Pin A","Leer Pin B","Leer Pin C"]
                for index in range(3):
                    btn_pin = Button(text='%s' % pins[index], size_hint_y=None, height=44)
                    btn_pin.bind(on_press=self.DynamicButton)
                    dropdownpin.add_widget(btn_pin)



                areamodules=Scatter(do_rotation=False, do_scale=False)
                areamodules=self.ids.areamodules
                areamodules.clear_widgets()

                led_on=Button(text='Encender Led', id='led_on', size_hint=(0.6,0.1), pos_hint={'x':0.2,'y':0.70}, background_color=(0,1,0,1),border=(20,20,20,20))
                led_on.bind(on_release=dropdownon.open)
                
                led_off=Button(text='Apagar Led', id='led_off', size_hint=(0.6,0.1), pos_hint={'x':0.2,'y':0.50}, background_color=(0,1,1,1))
                led_off.bind(on_release=dropdownoff.open)
                
                read_pin=Button(text='Leer Pin', id='read_pin', size_hint=(0.6,0.1), pos_hint={'x':0.2,'y':0.30}, background_color=(0,0,1,1))
                read_pin.bind(on_release=dropdownpin.open)

                areamodules.add_widget(led_on)
                areamodules.add_widget(led_off)
                areamodules.add_widget(read_pin)

        def fxled_on(Color):
            nfh = open("Compilador/Builder/temp/temp/temp.ino", "a")
            x = Modulo.Led_On(Color)
            nfh.write(x.write(0, ""))

        def fxled_off(Color):
            nfh = open("Compilador/Builder/temp/temp/temp.ino", "a")
            x = Modulo.Led_Off(Color)
            nfh.write(x.write(0, ""))

        def delay(Sec):
            nfh = open("Compilador/Builder/temp/temp/temp.ino", "a")
            x = Modulo.Delay(Sec)
            nfh.write(x.write(0, ""))




        def modcontrols(self):
                areamodules=self.ids.areamodules
                areamodules.clear_widgets()

                dropdowntime=DropDown()
                time = ["0,1s","0,2s","1s"]
                for index in range(3):
                    btn_time = Button(text='%s' % time[index], size_hint_y=None, height=44)
                    btn_time.bind(on_press=self.DynamicButton)
                    dropdowntime.add_widget(btn_time)

                control_if=Button(text='If(Condicion)', size_hint=(0.6,0.1), pos_hint={'x':0.2,'y':0.70}, background_color=(0,1,0,1))
                control_time=Button(text='Pause(time)', size_hint=(0.6,0.1), pos_hint={'x':0.2,'y':0.50},background_color=(0,1,1,1))
                control_while=Button(text='While(Condicion)', size_hint=(0.6,0.1), pos_hint={'x':0.2,'y':0.30},background_color=(0,0,1,1))

                control_time.bind(on_release=dropdowntime.open)

                areamodules.add_widget(control_if)
                areamodules.add_widget(control_time)
                areamodules.add_widget(control_while)


        def modopr(self):

                areamodules=self.ids.areamodules
                areamodules.clear_widgets()
                mod_sum=Button(text='()+()', size_hint=(0.5,0.1), pos_hint={'x':0.25,'y':0.75}, background_color=(0,1,1,1))
                subtraction=Button(text='()-()',size_hint=(0.5,0.1), pos_hint={'x':0.25,'y':0.65}, background_color=(0,1,1,1))
                multiplication=Button(text='()x()',size_hint=(0.5,0.1), pos_hint={'x':0.25,'y':0.55}, background_color=(0,1,1,1))
                division=Button(text='()/()',size_hint=(0.5,0.1), pos_hint={'x':0.25,'y':0.45}, background_color=(0,1,1,1))
                greater_than=Button(text='()>()',size_hint=(0.5,0.1), pos_hint={'x':0.25,'y':0.35}, background_color=(0,1,1,1))
                smaller_than=Button(text='()<()',size_hint=(0.5,0.1), pos_hint={'x':0.25,'y':0.25}, background_color=(0,1,1,1))
                same_that=Button(text='()==()',size_hint=(0.5,0.1), pos_hint={'x':0.25,'y':0.15}, background_color=(0,1,1,1))

                areamodules.add_widget(mod_sum)
                areamodules.add_widget(subtraction)
                areamodules.add_widget(multiplication)
                areamodules.add_widget(division)
                areamodules.add_widget(greater_than)
                areamodules.add_widget(smaller_than)
                areamodules.add_widget(same_that)




class MainApp(App):
        IDLE.FileBase() # Copia base a temp.ino
        title = "NEWTIDEIDLE"
        def build(self):
                self.IDLE=IDLE()
                return self.IDLE

if __name__ == "__main__":
        MainApp().run()
