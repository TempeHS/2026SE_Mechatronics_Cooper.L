from time import sleep
from machine import Pin, PWM
from servo import Servo
from movement import Movement


rwheel = Servo(pwm=PWM(15))
lwheel = Servo(pwm=PWM(16))
wheels = Movement(rwheel, lwheel)

class State():
    def __init__(self, rwheel, lwheel):
        self.__rservo = rwheel
        self.__lservo = lwheel
    def forward_state(self):
        wheels.forward()
    def idle_state(self):
        wheels.stop()
    def rotate_90_state(self):
        wheels.rrotate()
        sleep(1200)
        wheels.stop()
        sleep(200)
    def rotate_180_state(self):
        wheels.rrotate()
        sleep(1200)
        wheels.stop()
        sleep(200)
        wheels.rrotate()
        sleep(1200)
        wheels.stop()
        sleep(200)