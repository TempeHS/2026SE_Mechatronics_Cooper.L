from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from coloursensor import Scan

colourSensor = PiicoDev_VEML6040()
display = create_PiicoDev_SSD1306()
data = Scan(colourSensor)


while True:
    display.fill(0)
    display.text("PiicoDev",30,20, 1)
    display.text(str(data.scan()),50,35, 1)
    display.show()