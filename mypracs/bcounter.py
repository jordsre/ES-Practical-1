#!/usr/bin/python3
"""
Readjust this Docstring as follows:
Names: Jordan Ross-Elliott 
Student Number: RSSJOR002
Prac: 1
Date: 28/07/19
"""
# import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep 
import itertools

# set up board number convention and pins
GPIO.setmode(GPIO.BOARD)
LEDlist= (13,15,11) # LEDs
BInc = 29 # increment
BDec = 31 # decrement

# GPIO setup
GPIO.setup(LEDlist, GPIO.OUT)
GPIO.setup(BInc, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BDec, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
GPIO.output(LEDlist, False)

# create a counter to keep track of values
global counter
counter = 0

# create a list of binary numbers
n=3
my_list = list(itertools.product([0, 1], repeat=n))

# callback function for button increment 
def callback_inc(BInc):
    global counter
    counter += 1
    if counter<0:
        counter += 8
    if counter==8:
        counter=0

    GPIO.output(LEDlist,lst[counter]) 
    sleep(.2)
    print('Increment')

# callback function for button decrement
def callback_dec(BDec):
    global counter
    counter -= 1
    if counter<0:
        counter += 8
    if counter==8:
        counter=0

    GPIO.output(LEDlist,lst[counter])
    sleep(.2)
    print('Decrement')

# debounce and interupts
GPIO.add_event_detect(Binc, GPIO.FALLING, callback=callback_inc, bouncetime=200)
GPIO.add_event_detect(BDec, GPIO.FALLING, callback=callback_dec, bouncetime=200)

def main():
    pass

if __name__ == "__main__":
# Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except:
        print("Some other error occurred")


