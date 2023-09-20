"""
Created by: Ihor Chernyshev
Created on: Sep 2023
This program calculates the area and perimeter of a rectangle with dimensions 5 cm & 3 cm
"""

from microbit import *
from time import sleep


display.clear()
sleep(1)

display.scroll("Perimeter = " + str(2 * 5 + 2 * 3))
display.clear()
sleep(1)
display.scroll("Area = " + str(5 * 3))
