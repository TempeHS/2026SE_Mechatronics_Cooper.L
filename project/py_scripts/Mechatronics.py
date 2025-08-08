import time
from machine import Pin, PWM
from servo import Servo
from test import Movement
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

rwheel = Servo(pwm=PWM(15))
lwheel = Servo(pwm=PWM(16))

wheels = Movement(rwheel, lwheel)
'''
while True:
    wheels.forward()
    time.sleep(3)
    wheels.backward()
    time.sleep(3)
'''
"""
wheels.rotate()
time.sleep(1.5)
wheels.stop()
"""
range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 1]) 

while True:
    if range_a.distance_mm > 300:
        wheels.fforward()
    elif range_a.distance_mm > 200:
        wheels.forward()
    elif range_a.distance_mm > 150:
        wheels.sforward()
    elif range_a.distance_mm < 100:
        wheels.backward()
    elif range_a.distance_mm == 100:
        wheels.rotate()
        time.sleep(1.5)
