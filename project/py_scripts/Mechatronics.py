from time import sleep
from machine import Pin, PWM
from servo import Servo
from movement import Movement
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


'''
while True:
    if range_a.distance_mm > 200:
        wheels.fforward()
    elif range_a.distance_mm > 150:
        wheels.forward()
    elif range_a.distance_mm > 125:
        wheels.sforward()
    elif range_a.distance_mm <= 100:
        wheels.rotate()
        time.sleep(1.5)
'''
'''
while True:
    wheels.forward()
    if range_b.distance_mm < 100:
        wheels.rotate()
        time.sleep(1.5)
        if range_a.distance_mm > 200:
            break
        else: 
            wheels.rotate()
            time.sleep(3)
    '''

while True:
    if range_a.distance_mm > 100:
        if range_b.distance_mm > 100:
            wheels.forward()
            sleep(1.1)
            wheels.rrotate()
            sleep(1.2)
            wheels.stop()
            sleep(1)
            if range_a.distance_mm <= 100:
                wheels.rrotate()
                sleep(1.2)
                wheels.stop()
                sleep(0.2)
                wheels.rrotate()
                sleep(1.2)
                wheels.stop()
                sleep(0.2)
            else:
                wheels.forward()
                sleep(1)
                
    elif range_a.distance_mm <= 100:
        wheels.rrotate()
        sleep(1.2)
        wheels.stop()
        sleep(0.2)
        wheels.rrotate()
        sleep(1.2)
        wheels.stop()
        sleep(0.2)
        wheels.backward()
        sleep(0.3)
        if range_b.distance_mm > 100:
            wheels.rrotate()
            sleep(1.2)
            wheels.stop()
            sleep(0.2)


