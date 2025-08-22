from time import sleep
from machine import Pin, PWM
from servo import Servo
from project.lib.movement import Movement
from states import State



servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))
rightwheel = Servo(servo_pwm_left)
leftwheel = Servo(servo_pwm_right)
wheels = State(leftwheel, rightwheel)

while True:
    wheels.forward_state()
    sleep(2)
    wheels.rotate_90_state()
    sleep(2)
    wheels.idle_state()
    sleep(2)
    wheels.rotate_180_state()
    sleep(2)