import os


class Compiler():
    def __init__(self, system):
        self.path = os.path.abspath(__file__)
        self.path = os.path.dirname(self.path)
        self.path = self.path + "/Compilador"
        self.path = os.path.abspath(self.path)
        self.libraries = self.path + "/libraries"
        self.libraries = os.path.abspath(self.libraries)
        self.build_path = self.path + "/temp/build"
        self.build_path = os.path.abspath(self.build_path)
        self.sketch = self.path + "/temp/temp.ino"
        self.sketch = os.path.abspath(self.sketch)
        self.hex = self.path + "/temp/build/temp.ino.hex"
        self.hex = os.path.abspath(self.hex)
        self.path = self.path + "/" + system
        self.path = os.path.abspath(self.path)
        self.arduino_builder = self.path + "/arduino-builder"
        self.arduino_builder = os.path.abspath(self.arduino_builder)
        self.hardware = self.path + "/hardware"
        self.hardware = os.path.abspath(self.hardware)
        self.tools_builder = self.path + "/tools-builder)
        self.tools_builder = os.path.abspath(self.tools_builder)
        self.tools_avr = self.path + "/hardware/tools/avr"
        self.tools_avr = os.path.abspath(self.tools_avr)
        self.built_in_libraries = self.path + "/libraries"
        self.built_in_libraries = os.path.abspath(self.built_in_libraries)
        self.avrdude = self.path + "/hardware/tools/bin/avrdude"
        self.avrdude = os.path.abspath(self.avrdude)
        self.avrdude_conf = self.path + "/hardware/tools/avr/etc/avrdude.conf"
        self.avrdude_conf = os.path.abspath(self.avrdude_conf)

    def dump_prefs(self):
        cmd = "%s -dump-prefs -logger=machine -hardware %s -tools %s -tools %s -built-in-libraries %s -libraries %s -fqbn=arduino:avr:uno -ide-version=10805 -build-path %s -warnings=all -build-cache %s -prefs=build.warn_data_percentage=75 -pref=runtime.tools.avr-gcc.path=%s -prefs=runtime.tools.aruinoOTA.path=%s -prefs=runtime.tools.avrdude.path=%s -verbose %s" % (self.arduino_builder, self.hardware, self.tools_builder, self.tools_avr, self.libraries, self.libraries, self.build_path, self.sketch, self.tools_avr, self.tools_avr, self.tools_avr, self.hex)
        return os.system(cmd)
    def compile(self):
        cmd = "%s -compile -logger=machine -hardware %s -tools %s -tools %s -built-in-libraries %s -libraries %s -fqbn=arduino:avr:uno -ide-version=10805 -build-path %s -warnings=all -build-cache %s -prefs=build.warn_data_percentage=75 -pref=runtime.tools.avr-gcc.path=%s -prefs=runtime.tools.aruinoOTA.path=%s -prefs=runtime.tools.avrdude.path=%s -verbose %s" % (self.arduino_builder, self.hardware, self.tools_builder, self.tools_avr, self.libraries, self.libraries, self.build_path, self.sketch, self.tools_avr, self.tools_avr, self.tools_avr, self.hex)
        return os.system(cmd)
    def send(self, port):
        cmd = "%s -C%s -v -patmega328p -carduino -P%s -b115200 -D -Uflash:w:%s:i " % (self.avrdude, self.avrdude_conf, port, self.hex)
        return os.system(cmd)
