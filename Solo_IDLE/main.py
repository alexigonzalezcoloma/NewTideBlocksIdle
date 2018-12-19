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
from kivy.uix.dropdown import DropDown
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.scatter import Scatter
global nbtn
xpos = 0.1; ypos = 0.85
import os, sys; sys.path.insert(0, 'Modulo'); import Modulo;
from Compilador import Compilador
global nbtn
nbtn = 0
global abtn; abtn = []
global afnc; afnc = []
#import time
xpos = 0.1; ypos = 0.85
import serial.tools.list_ports

class IDLE(BoxLayout):

        def PreComp(aFx):
                nfh = open("Compilador/Builder/temp/temp/temp.ino", "a")
                tab = 0
                for e in aFx:
                        if e == "Encender blanco":
                                x = Modulo.Led_On("13")

                        if e == "Encender rojo":
                                x = Modulo.Led_On("4")

                        if e == "Encender verde":
                                x = Modulo.Led_On("6")

                        if e == "Encender amarillo":
                                x = Modulo.Led_On("5")

                        if e == "Apagar blanco":
                                x = Modulo.Led_Off("13")

                        if e == "Apagar rojo":
                                x = Modulo.Led_Off("4")

                        if e == "Apagar verde":
                                x = Modulo.Led_Off("6")

                        if e == "Apagar amarillo":
                                x = Modulo.Led_Off("5")

                        if e == "Pause(1s)":
                                x = Modulo.Delay(1000)

                        if e == "1 vez":
                                x = Modulo.While(1)
                                tab = 1

                        if e == "2 veces":
                                x = Modulo.While(2)

                        if e == "3 veces":
                                x = Modulo.While(3)

                        nfh.write(x.write(tab, ""))
                nfh.close()

        def Repaint(self):
                programarea = self.ids.areamodulesprogram

                for l in abtn:
                        #print(abtn)
                        programarea.remove_widget(l)
                #time.sleep(1)
                for j in abtn:
                        #print(abtn)
                        programarea.add_widget(j)
                        
        def DynamicButton(self, instance):
                global abtn, xpos, ypos, nbtn

                btext = instance.text
                bcolor = instance.background_color

                self.dbtn = Button(text=btext, id=str(nbtn),
                              size_hint=(0.25,0.1), pos_hint={'x':xpos,'y':ypos},
                              background_color=bcolor)
                self.dbtn.bind(on_press=self.DynamicClear)

                if ypos > 0.15 and xpos < 1:
                        ypos -= 0.10
                        nbtn += 1
                elif xpos < 1:
                        nbtn += 1
                        xpos += 0.3
                        ypos = 0.85
                abtn.append(self.dbtn)
                afnc.append(btext)
                self.Repaint()

        def DynamicClear(self, instance):
                global abtn, ypos, nbtn
                programarea = self.ids.areamodulesprogram
                index = int(instance.id)
                aux = abtn[index].pos[1]
                for k in range(index, len(abtn)):
                        abtn[k].id = str(k-1)
                        #print(abtn[k].pos)
                        abtn[k].pos = [abtn[k].pos[0], aux]
                        aux = abtn[k].pos[1]
                        #print(abtn[k].pos)
                ypos += 0.10
                nbtn -= 1
                programarea.remove_widget(abtn[index])
                abtn.pop(index)
                afnc.pop(index)
                self.Repaint()

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
                IDLE.PreComp(afnc)

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


        def modmakers(self):
                dropdownon = DropDown()
                Colors = ["Encender blanco","Encender rojo","Encender verde","Encender amarillo"]
                for index in range(4):
                    btnon = Button(text='%s' % Colors[index], size_hint_y=None, height=44)
                    btnon.bind(on_press=self.DynamicButton)
                    dropdownon.add_widget(btnon)

                dropdownoff = DropDown()
                Colors = ["Apagar blanco","Apagar rojo","Apagar verde","Apagar amarillo"]
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

        def modcontrols(self):
                areamodules=self.ids.areamodules
                areamodules.clear_widgets()

                dropdownrep=DropDown()
                times = ["1 vez","2 veces","3 veces"]
                for index in range(3):
                    btn_rep = Button(text='%s' % times[index], size_hint_y=None, height=44)
                    btn_rep.bind(on_press=self.DynamicButton)
                    dropdownrep.add_widget(btn_rep)

                control_if=Button(text='If(Condicion)', size_hint=(0.6,0.1), pos_hint={'x':0.2,'y':0.70}, background_color=(0,1,0,1))
                control_time=Button(text='Pause(1s)', size_hint=(0.6,0.1), pos_hint={'x':0.2,'y':0.50},background_color=(0,1,1,1))
                control_while=Button(text='Repetir', size_hint=(0.6,0.1), pos_hint={'x':0.2,'y':0.30},background_color=(0,0,1,1))

                control_time.bind(on_release=self.DynamicButton)
                control_while.bind(on_release=dropdownrep.open)

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
