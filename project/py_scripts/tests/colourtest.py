from coloursensor import c
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from display import Display

colourSensor = PiicoDev_VEML6040() # initialise the sensor
data = Scan(colourSensor)

while True:
    data.display()