from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms


class Display():
    def __init__(self, display):
        self.__display = display
    def showtext(self, text):
        self.__display.fill(0)
        self.__display.text(str(text), 50, 35, 1)
        self.__display.show()