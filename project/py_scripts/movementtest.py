from time import sleep
from machine import Pin, PWM
from servo import Servo
from movement import Movement



servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))

Movement(servo_pwm_left, servo_pwm_right, debug=False)

while True:
    Movement.forward()
    sleep(3)
    Movement.back()
    sleep(3)