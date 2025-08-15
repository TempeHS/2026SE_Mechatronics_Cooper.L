from time import sleep
from machine import Pin, PWM
from servo import Servo
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 1])
class UltrasonicSensor:
    def __init__(self, fsensor, ssensor):
        self.__fsensor = range_a
        self.__fsensor = range_b
    def frontscan():
        
    