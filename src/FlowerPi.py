#!/usr/bin/env python

from time import sleep
from Hardware import Hardware
from datetime import datetime
from astral import Astral


class FlowerPi(object):
    
    def __init__(self):
        self.hardware = Hardware()
        a = Astral()
        a.solar_depression = 'civil'
        self.city = a['Kiev']
        
        
    def process(self):
        now = datetime.now()
        print("Processing... Current time: {}".format(str(now)))
        
        sun = self.city.sun(date=now, local=True)
        sunrise = sun['sunrise']
        sunset = sun['sunset']
        
        if sunrise.hour == now.hour and sunrise.minute == now.minute:
            print("Sunrise. Time: {}".format(str(now)))
            self.hardware.turn_lamp_low()
            
        if sunset.hour == now.hour and sunset.minute == now.minute:
            print("Sunset. Time: {}".format(str(now)))
            self.hardware.turn_lamp_off()
            

def main():
    try:
        flower_pi = FlowerPi()
        while True:
            flower_pi.process()
            sleep(30)
    except KeyboardInterrupt:
        print("Stop processing")
            

if __name__ == "__main__": 
    main()