from time import sleep
from machine import Pin, PWM
from servo import Servo
from states import State
from movement import Movement
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

rwheel = Servo(PWM(Pin(15)))
lwheel = Servo(PWM(Pin(16)))
state = State(lwheel, rwheel)
range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[1, 0, 0, 0]) 

servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))
rightwheel = Servo(servo_pwm_left)
leftwheel = Servo(servo_pwm_right)
wheels = Movement(rightwheel, leftwheel)
while True:
    wheels.forward()
    if range_a.distance_mm > 100:
        if range_b.distance_mm > 100:
            wheels.forward()
            sleep(1.1)
            wheels.rrotate()
            sleep(1200)
            wheels.stop()
            sleep(200)
            if range_a.distance_mm <= 100:
                wheels.rrotate()
                sleep(1200)
                wheels.stop()
                sleep(200)
                wheels.rrotate()
                sleep(1200)
                wheels.stop()
                sleep(200)
            else:
                wheels.forward()
        else:
            wheels.forward()
            sleep(1)
    else:
        wheels.rrotate()
        sleep(1200)
        wheels.stop()
        sleep(200)
        wheels.rrotate()
        sleep(1200)
        wheels.stop()
        sleep(200)
        if range_b.distance_mm > 100:
            wheels.rrotate()
            sleep(1200)
            wheels.stop()
            sleep(200)


