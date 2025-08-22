from time import sleep
from machine import Pin, PWM
from servo import Servo
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_SSD1306 import *
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from movement import Movement
from states import State
from coloursensor import ColourScan
from display import Display

rwheel = Servo(pwm=PWM(15))
lwheel = Servo(pwm=PWM(16))
state = State(rwheel, lwheel)
range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 1]) 
colourSensor = PiicoDev_VEML6040()
screen = create_PiicoDev_SSD1306()
data = ColourScan(colourSensor)
oled = Display(screen)

while True:
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


