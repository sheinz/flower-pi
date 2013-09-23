'''
Created on Sep 24, 2013

@author: yura
'''

import RPIO as GPIO

class Hardware(object):
    '''
    classdocs
    '''

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(25, GPIO.OUT, initial=GPIO.HIGH)
        
    
    def turn_lamp_off(self):
        GPIO.output(24, True);
        GPIO.output(25, True);
        
    def turn_lamp_low(self):
        GPIO.output(24, False);
        GPIO.output(25, True);
        
    def turn_lamp_medium(self):
        GPIO.output(24, True);
        GPIO.output(25, False);
        
    def turn_lamp_high(self):
        GPIO.output(24, False);
        GPIO.output(25, False);
        
        