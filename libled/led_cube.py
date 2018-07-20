import os
from ctypes import *
import sys
import platform
import util.logger as logger

LED_HEIGHT = 32
LED_WIDTH = 16
LED_DEPTH = 8

dirname = os.path.dirname(__file__)
if sys.platform == 'darwin':
    ledlib = dirname + '/libledLib.dylib'
elif sys.platform == 'win32':
    arch = platform.architecture()[0]
    if arch == '64bit':
        ledlib = dirname + '/ledLib64.dll'
    else:
        ledlib = dirname + '/ledLib32.dll'
elif 'linux' in sys.platform and platform.machine() == 'armv7l':
    ledlib = dirname + '/ledLibarmv7l.so' # for Raspberry PI3
else:
    raise NotImplementedError('Unsupported OS.' + sys.platform)

logger.i('LoadLibrary: '+ ledlib)

def local_split_url_and_port(url):
    result = url.split(":")
    if len(result) > 2:
        raise ArgumentError('invalid url format.')
    else:
        try:
            if len(result) == 2:
                return result[0], int(result[1])
            else:
                return url, None
        except ValueError:
            raise ArgumentError('invalid port number')


class LedCube(object):
    def __init__(self, led):
        self.led = led

    def Show(self):
        #print("led.Show()")
        self.led.Show()

    def SetUrl(self, dest):
        print("led.SetUrl():" + dest)
        url, port = local_split_url_and_port(dest)

        self.led.SetUrl(url)
        if port is not None:
            print("led.SetPort():" + str(port))
            self.led.SetPort(port)

    def Clear(self):
        #print("led.Clear()")
        self.led.Clear()
    
    def SetLed(self, x, y, z, color):
        # print("led.SetLed()") comment out for performance
        self.led.SetLed(x, y, z, color)
    
    def Wait(self, msec):
        self.led.Wait(int(msec))

    def EnableSimulator(self, is_enable):
        self.led.EnableSimulator(is_enable)

led = LedCube(cdll.LoadLibrary(ledlib))
