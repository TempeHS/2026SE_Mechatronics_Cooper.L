from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from coloursensor import ColourScan



while True:
    display.fill(0)
    display.text(str(data.ColourScan()),50,35, 1)
    display.show()

class Display:
    def init__(self, display, debug):
        self.__display = display
    def display(self, text):
        display.fill(0)
        display.text(str(text), 50, 35, 1)
        display.show()
        

        
