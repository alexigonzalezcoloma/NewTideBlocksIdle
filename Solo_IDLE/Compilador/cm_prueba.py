import os
import sys; sys.path.insert(0, 'Traductor');
class Compilador():
    def __init__(self, system):
        self.path = os.path.abspath(__file__)
        self.path = os.path.dirname(self.path)
        self.path = self.path + "/Compilador/arduino-builder"
        self.path = os.path.abspath(self.path)
        self.libraries = self.path + "/libraries"
        self.libraries = os.path.abspath(self.libraries)
        self.path = os.path.abspath(__file__)
        self.path = os.path.dirname(self.path)
        self.path = self.path + "/Compilador"
        self.build_path = self.path + "/temp/build"
        self.build_path = os.path.abspath(self.build_path)
        self.sketch = self.path + "/temp"
        self.sketch = os.path.abspath(self.sketch)
        self.sketchF = self.path + "/temp/temp.ino"
        self.sketchF = os.path.abspath(self.sketchF)
        self.hex = self.path + "/temp/build/temp.ino.hex"
        self.hex = os.path.abspath(self.hex)
        self.path = self.path + "/arduino-builder"
        self.arduino_builder = self.path
        self.arduino_builder = os.path.abspath(self.arduino_builder)
        print (self.arduino_builder)
        self.hardware = self.path + "/hardware"
        self.hardware = os.path.abspath(self.hardware)
        self.tools_builder = self.path + "/tools-builder"
        self.tools_builder = os.path.abspath(self.tools_builder)
        self.tools_avr = self.path + "/hardware/tools/avr"
        self.tools_avr = os.path.abspath(self.tools_avr)
        self.built_in_libraries = self.path + "/libraries"
        self.built_in_libraries = os.path.abspath(self.built_in_libraries)
        self.avrdude = self.path + "/hardware/tools/bin/avrdude.exe"
        self.avrdude = os.path.abspath(self.avrdude)
        self.avrdude_conf = self.path + "/hardware/tools/avr/etc/avrdude.conf"
        self.avrdude_conf = os.path.abspath(self.avrdude_conf)
        #ultimo parametro direccion del archivo

    def dump_prefs(self):
        cmd = "C:\\Users\\Mathias\\Documents\\GitHub\\NewTideBlocksIdle\\Traductor\\Compilador\\Compilador\\arduino-builder\\arduino-builder.exe -dump-prefs -logger=machine -hardware %s -tools %s -tools %s -built-in-libraries %s -libraries %s -fqbn=arduino:avr:uno -ide-version=10805 -build-path %s -warnings=all -build-cache %s -prefs=build.warn_data_percentage=75 -prefs=runtime.tools.arduinoOTA.path=%s -prefs=runtime.tools.avr-gcc.path=%s -prefs=runtime.tools.avrdude.path=%s -verbose %s" %(self.hardware, self.tools_builder, self.tools_avr, self.libraries, self.libraries, self.build_path, self.sketch, self.tools_avr, self.tools_avr, self.tools_avr, self.sketchF)
        #cmd = "C:\\Program Files\\WindowsApps\\ArduinoLLC.ArduinoIDE_1.8.15.0_x86__mdqgnx93n4wtt\\arduino-builder -dump-prefs -logger=machine -hardware C:\\Program Files\\WindowsApps\\ArduinoLLC.ArduinoIDE_1.8.15.0_x86__mdqgnx93n4wtt\\hardware -tools C:\\Program Files\\WindowsApps\\ArduinoLLC.ArduinoIDE_1.8.15.0_x86__mdqgnx93n4wtt\\tools-builder -tools C:\\Program Files\\WindowsApps\\ArduinoLLC.ArduinoIDE_1.8.15.0_x86__mdqgnx93n4wtt\\hardware\\tools\\avr -built-in-libraries C:\\Program Files\\WindowsApps\\ArduinoLLC.ArduinoIDE_1.8.15.0_x86__mdqgnx93n4wtt\\libraries -libraries C:\\Users\\Mathias\\Documents\\Arduino\\libraries -fqbn=arduino:avr:uno -ide-version=10807 -build-path C:\\Users\\Mathias\\AppData\\Local\\Temp\\arduino_build_729625 -warnings=none -build-cache C:\\Users\\Mathias\\AppData\\Local\\Temp\\arduino_cache_757832 -prefs=build.warn_data_percentage=75 -prefs=runtime.tools.avrdude.path=C:\\Program Files\\WindowsApps\\ArduinoLLC.ArduinoIDE_1.8.15.0_x86__mdqgnx93n4wtt\\hardware\\tools\\avr -prefs=runtime.tools.avrdude-6.3.0-arduino14.path=C:\\Program Files\\WindowsApps\\ArduinoLLC.ArduinoIDE_1.8.15.0_x86__mdqgnx93n4wtt\hardware\tools\avr -prefs=runtime.tools.avr-gcc.path=C:\Program Files\WindowsApps\ArduinoLLC.ArduinoIDE_1.8.15.0_x86__mdqgnx93n4wtt\hardware\tools\avr -prefs=runtime.tools.avr-gcc-5.4.0-atmel3.6.1-arduino2.path=C:\Program Files\WindowsApps\ArduinoLLC.ArduinoIDE_1.8.15.0_x86__mdqgnx93n4wtt\hardware\tools\avr -prefs=runtime.tools.arduinoOTA.path=C:\Program Files\WindowsApps\ArduinoLLC.ArduinoIDE_1.8.15.0_x86__mdqgnx93n4wtt\hardware\tools\avr -prefs=runtime.tools.arduinoOTA-1.2.1.path=C:\Program Files\WindowsApps\ArduinoLLC.ArduinoIDE_1.8.15.0_x86__mdqgnx93n4wtt\hardware\tools\avr -verbose C:\Users\Mathias\Desktop\Internet Explorer\universidad\2018\2 semestre\\taller III\\codigos arduino\\sketch_oct23a\\sketch_oct23a.ino"
        return os.system(cmd)
    def compilate(self):
        cmd = "%s -compile -logger=machine -hardware %s -tools %s -tools %s -built-in-libraries %s -libraries %s -fqbn=arduino:avr:uno -ide-version=10805 -build-path %s -warnings=all -build-cache %s -prefs=build.warn_data_percentage=75 -pref=runtime.tools.avr-gcc.path=%s -prefs=runtime.tools.aruinoOTA.path=%s -prefs=runtime.tools.avrdude.path=%s -verbose %s" % (self.arduino_builder, self.hardware, self.tools_builder, self.tools_avr, self.libraries, self.libraries, self.build_path, self.sketch, self.tools_avr, self.tools_avr, self.tools_avr, self.hex)
        return os.system(cmd)
    def send(self, port):
        cmd = "%s -C%s -v -patmega328p -carduino -P%s -b115200 -D -Uflash:w:%s:i " % (self.avrdude, self.avrdude_conf, port, self.hex)
        return os.system(cmd)

x=Compilador(os.system)
x.dump_prefs()
