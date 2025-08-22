from coloursensor import ColourScan
from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
from PiicoDev_VEML6040 import PiicoDev_VEML6040


colourSensor = PiicoDev_VEML6040()
display = create_PiicoDev_SSD1306()
data2 = ColourScan.scan()

class Display:
    def __init__(self, display, text):
        self.__display = display
        self.__text = text
    def showscreen(self, text):
        display.fill(0)
        display.text(str(text), 50, 35, 1)
        display.show()


