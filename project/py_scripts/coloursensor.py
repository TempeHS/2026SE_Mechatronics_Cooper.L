class ColourScan():
    def __init__(self, sensor):
        self.__sensor = sensor
    def scan(self):
        data = self.__sensor.readHSV()
        hue = data["hue"]
        if 100 > hue > 75:
            return "Green"
        else:
            return "Not Green"