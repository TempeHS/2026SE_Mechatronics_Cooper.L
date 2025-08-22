from time import sleep
from machine import Pin, PWM
from servo import Servo
from movement import Movement

servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))
rightwheel = Servo(servo_pwm_left)
leftwheel = Servo(servo_pwm_right)
wheels = Movement(rightwheel, leftwheel)

while True:
    wheels.forward()
    sleep(3)
    wheels.backward()
    sleep(3)
    wheels.stop()
    sleep(3)
    wheels.rrotate()
    sleep(3)
    wheels.lrotate()
    sleep(3)