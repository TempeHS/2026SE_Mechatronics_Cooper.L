import time
from machine import Pin, PWM
from servo import Servo


# create a PWM servo controller (16 - pin Pico)
servo_pwm_l = PWM(Pin(16))
servo_pwm_r = PWM(Pin(15))

# Set the parameters of the servo pulses, more details in the "Documentation" section
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500


'''
while True:
    # manually set the servo duty time
    servo_l.set_duty(1400)
    servo_r.set_duty(1600)
    time.sleep(2)

    servo_l.set_duty(1600)
    servo_r.set_duty(1400)
    time.sleep(2)

    servo_l.stop()
    servo_r.stop()
    time.sleep(2)
'''
class Movement_test:
    def __innit(self, servo_l, servo_r, debug=False):
        self.__servo_left = servo_l
        self.__servo_right = servo_r
    def forward(self):
        self.__servo_left.set_duty(1350)
        self.__servo_right.set_duty(1650)
    def fast(self):
        self.__servo_left.set_duty(1000)
        self.__servo_right.set_duty(2000) 
    def back(self):
        self.__servo_left.set_duty(1650)
        self.__servo_right.set_duty(1350)

while True:
    Movement_test.forward()
    sleep(3)
    Movement_test.back()
    sleep(3)