import os
import sys; sys.path.insert(0, 'Traductor');
class Compilador():
    def __init__(self, system): 
        self.path = os.path.abspath(__file__)
        self.path = os.path.dirname(self.path)
        self.path = self.path + "/Builder/arduino-builder"
        self.path = os.path.abspath(self.path)
        self.libraries = self.path + "/libraries"
        self.libraries = os.path.abspath(self.libraries)
        self.path = os.path.abspath(__file__)
        self.path = os.path.dirname(self.path)
        self.path = self.path + "/Builder"
        self.build_path = self.path + "/temp/build"
        self.build_path = os.path.abspath(self.build_path)
        self.build_cache = self.path + "/temp/temp"
        self.build_cache = os.path.abspath(self.build_cache)
        self.sketch = self.path + "/temp/temp/temp.ino"
        self.sketch = os.path.abspath(self.sketch)
        self.hex = self.path + "/temp/build/temp.ino.hex"
        self.hex = os.path.abspath(self.hex)
        self.path = self.path + "/arduino-builder"
        self.arduino_builder = self.path+"/arduino-builder.exe"
        self.arduino_builder = os.path.abspath(self.arduino_builder)
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
        #Lo anterior no es más que definiciones de direcciones a las que el compilador debe acceder para poder compilar
        #-build-cache string: Las compilaciones de 'core.a' se guardan en esta carpeta para ser almacenadas en caché y reutilizadas
        #-build-options-file string: En lugar de especificar - hardware, --tools, etc. cada vez, puede cargar todas estas opciones desde un archivo
        #-build-path string: Ruta del build
        #-built-in-libraries value: Especifique una carpeta 'bibliotecas' incorporada. Estas son las bibliotecas de baja prioridad. Se puede agregar varias veces para especificar múltiples carpetas 'bibliotecas' integradas
        #-code-complete-at string: Código completo de salida para boceto en una ubicación específica. El formato de ubicación es "file:line:col"
        #-compile: Compila el boceto dado
        #-core-api-version string: Versión de las API principales (utilizadas para completar ARDUINO #define) (por defecto "10600")
        #-daemon: Sirve sus funciones a través de rpc
        #-debug-level int: Activa los mensajes de depuración. Cuanto más alto, más chattier (por defecto 5)
        #-dump-prefs: Vuelca las propiedades de compilación utilizadas al compilar
        #-experimental: Permite características experimentales
        #-fqbn string: Nombre de placa completo
        #-hardware value: especifique una carpeta 'hardware'. Se puede agregar varias veces para especificar múltiples carpetas de 'hardware'
        #-ide-version string: [en desuso] Use 'core-api-version' en su lugar (por defecto "10600")
        #-jobs int: Especifique cuántos procesos gcc concurrentes deben ejecutarse al mismo tiempo. El valor predeterminado es el número de núcleos disponibles en la máquina en ejecución
        #-libraries value: Especifique una carpeta 'bibliotecas'. Se puede agregar varias veces para especificar múltiples carpetas 'bibliotecas'
        #-logger string: Establece el tipo de registrador. Los valores disponibles son 'human', 'humantags', 'máquina' (por defecto "human")
        #-prefs value: Especifique una preferencia personalizada. Se puede agregar varias veces para especificar múltiples preferencias personalizadas
        #-preprocess: preprocesar el boceto dado
        #-quiet: Si 'true' no imprime ninguna advertencia, progreso o lo que sea
        #-tools value: Especifique una carpeta 'tools'. Se puede agregar varias veces para especificar múltiples carpetas de 'tools'
        #-trace: Rastrea todo el ciclo de vida del proceso
        #-verbose: Si 'true' imprime muchas cosas
        #-version: Imprime version y sale
        #-vid-pid string: Especifique usar propiedades de compilación específicas de vid / pid, como se define en boards.txt
        #-warnings string: Establece el nivel de advertencias. Los valores disponibles son 'none', 'default', 'more' y 'all'
    def dump_prefs(self):
        cmd = "%s -dump-prefs -logger=machine -hardware %s -tools %s -tools %s -built-in-libraries %s -libraries %s -fqbn=arduino:avr:uno -ide-version=10807 -build-path %s -warnings=none -build-cache %s -prefs=build.warn_data_percentage=75 -prefs=runtime.tools.avrdude.path=%s -prefs=runtime.tools.avrdude-6.3.0-arduino14.path=%s -prefs=runtime.tools.avr-gcc.path=%s -prefs=runtime.tools.avr-gcc-5.4.0-atmel3.6.1-arduino2.path=%s -prefs=runtime.tools.arduinoOTA.path=%s -prefs=runtime.tools.arduinoOTA-1.2.1.path=%s -verbose %s" %(self.arduino_builder,self.hardware,self.tools_builder,self.tools_avr,self.built_in_libraries,self.libraries,self.build_path,self.build_cache,self.tools_avr,self.tools_avr,self.tools_avr,self.tools_avr,self.tools_avr,self.tools_avr,self.sketch)
        return os.system(cmd)
    def compilate(self):
        cmd = "%s -compile -logger=machine -hardware %s -tools %s -tools %s -built-in-libraries %s -libraries %s -fqbn=arduino:avr:uno -ide-version=10807 -build-path %s -warnings=none -build-cache %s -prefs=build.warn_data_percentage=75 -prefs=runtime.tools.avrdude.path=%s -prefs=runtime.tools.avrdude-6.3.0-arduino14.path=%s -prefs=runtime.tools.avr-gcc.path=%s -prefs=runtime.tools.avr-gcc-5.4.0-atmel3.6.1-arduino2.path=%s -prefs=runtime.tools.arduinoOTA.path=%s -prefs=runtime.tools.arduinoOTA-1.2.1.path=%s -verbose %s" %(self.arduino_builder,self.hardware,self.tools_builder,self.tools_avr,self.built_in_libraries,self.libraries,self.build_path,self.build_cache,self.tools_avr,self.tools_avr,self.tools_avr,self.tools_avr,self.tools_avr,self.tools_avr,self.sketch)
        return os.system(cmd)
    def send(self, port):
        cmd = "%s -C%s -v -patmega328p -carduino -P%s -b115200 -D -Uflash:w:%s:i " % (self.avrdude, self.avrdude_conf, port, self.hex)
        return os.system(cmd)
