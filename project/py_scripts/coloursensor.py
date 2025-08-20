from time import sleep
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function


# while True:
#     data = colourSensor.readHSV() # Read the sensor (Colour space: Hue Saturation Value)
#     hue = data['hue'] # extract the Hue information from data
#     label = colourSensor.classifyHue() # Read the sensor again, this time classify the colour
#     sleep(0.1)
#     print(str(label) + " Hue: " + str(hue)) # Show the label and the corresponding hue
#     if 100 > float(str(hue)) > 80:
#         print("Green")
#     else:
#         print("Not Green")

class Scan:
    def __init__(self, sensor):
        self.__sensor = sensor
    def scan(self):
        if 100 > self.__sensor > 80:
            return "Green"
        else:
            return "Not Green"