from time import sleep
from machine import Pin, PWM
from servo import Servo
from movement import Movement
from states import State
#from coloursensor import ColourScan
#from display import Display
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

rwheel = Servo(pwm=PWM(15))
lwheel = Servo(pwm=PWM(16))
state = State(rwheel, lwheel)
range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[1, 0, 0, 0]) 

while True:
    state.forward_state()
    if range_a.distance_mm > 100:
        if range_b.distance_mm > 100:
            state.forward_state()
            sleep(1.1)
            state.rotate_90_state()
            if range_a.distance_mm <= 100:
                state.rotate_180_state()
            else:
                state.forward_state()
        else:
            state.forward_state()
            sleep(1)
    else:
        state.rotate_180_state()
        if range_b.distance_mm > 100:
            state.rotate_90_state()


