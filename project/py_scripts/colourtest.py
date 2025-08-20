from coloursensor import Scan
from PiicoDev_VEML6040 import PiicoDev_VEML6040

colourSensor = PiicoDev_VEML6040() # initialise the sensor
data = Scan(colourSensor)

while True:
    print(str(data.scan()))