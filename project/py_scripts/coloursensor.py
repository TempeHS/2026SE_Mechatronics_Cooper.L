from time import sleep
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function


colourSensor = PiicoDev_VEML6040() # initialise the sensor

while True:
    data = colourSensor.readHSV() # Read the sensor (Colour space: Hue Saturation Value)
    hue = data['hue'] # extract the Hue information from data
    label = colourSensor.classifyHue() # Read the sensor again, this time classify the colour
    sleep(0.1)
    print(str(label) + " Hue: " + str(hue)) # Show the label and the corresponding hue
    if 90 > float(str(hue)) > 75:
        print("Green")