#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Jordan Ross-Elliott
Student Number: RSSJOR002
Prac: 1
Date: 22/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep

# pin numbers
button1 = 11
LED1 = 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED1,GPIO.OUT) # LED 1
GPIO.setup(button1,GPIO.IN, pull_up_down=GPIO.PUD_UP) # pushbutton
 

# GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=callback_method(),bouncetime=300)

# Logic that you write
def main():

	GPIO.output(LED1,GPIO.input(button1))
	sleep(.1)
# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:

       while True:
            main()

    except KeyboardInterrupt:
    	print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.output(LED1,False)
	GPIO.cleanup()

    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)



