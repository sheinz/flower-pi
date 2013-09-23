#!/usr/bin/env python

from time import sleep

def process():
    print("Processing...")

def main():
    try:
        while True:
            process()
            sleep(5)
    except KeyboardInterrupt:
        print("Stop processing")
            

if __name__ == "__main__": 
    main()