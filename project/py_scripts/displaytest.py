from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from coloursensor import ColourScan
from display import Display


colourSensor = PiicoDev_VEML6040()
display = create_PiicoDev_SSD1306()
data2 = ColourScan(colourSensor)

oled = Display(display)

while True:
    oled.display(green)