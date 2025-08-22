from time import sleep

class Movement():
    def __init__(self, rwheel, lwheel):
        self.__rservo = rwheel
        self.__lservo = lwheel
    def backward(self):
        self.__rservo.set_duty(1650)
        self.__lservo.set_duty(1350)
    def fforward(self):
        self.__rservo.set_duty(500)
        self.__lservo.set_duty(2500)
    def sforward(self):
        self.__rservo.set_duty(1300)
        self.__lservo.set_duty(1700)
    def forward(self):
        self.__rservo.set_duty(1150)
        self.__lservo.set_duty(1850)
    def rrotate(self):
        self.__rservo.set_duty(1700)
        self.__lservo.set_duty(1700)
    def lrotate(self):
        self.__rservo.set_duty(1300)
        self.__lservo.set_duty(1300)
    def stop(self):
        self.__rservo.set_duty(1500)
        self.__lservo.set_duty(1500)