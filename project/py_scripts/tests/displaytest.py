from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from coloursensor import ColourScan
from display import Display


colourSensor = PiicoDev_VEML6040()
screen = create_PiicoDev_SSD1306()
data2 = ColourScan(colourSensor)

oled = Display(screen, data2)

while True:
    oled.showscreen(data2.scan())