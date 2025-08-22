from time import sleep
from machine import Pin, PWM
from servo import Servo
from movement import Movement


rwheel = Servo(pwm=PWM(15))
lwheel = Servo(pwm=PWM(16))

class State():
    def __init__(self, rwheel, lwheel):
        self.__rservo = rwheel
        self.__lservo = lwheel
        self.__wheels = Movement(self.__rservo, self.__lservo)
    def forward_state(self):
        self.__wheels.forward()
    def idle_state(self):
        self.__wheels.stop()
    def rotate_90_state(self):
        self.__wheels.rrotate()
        sleep(1200)
        self.__wheels.stop()
        sleep(200)
    def rotate_180_state(self):
        self.__wheels.rrotate()
        sleep(1200)
        self.__wheels.stop()
        sleep(200)
        self.__wheels.rrotate()
        sleep(1200)
        self.__wheels.stop()
        sleep(200)



        wheels.rrotate()
        sleep(1200)
        wheels.stop()
        sleep(200)
        wheels.rrotate()
        sleep(1200)
        wheels.stop()
        sleep(200)