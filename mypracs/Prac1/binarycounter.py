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

# Logic that you write
def main():
    print("write your logic here")


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
