"""
Created by: Ihor Chernyshev
Created on: Sep 2023
This program calculates the area and perimeter of a rectangle with dimensions 5 cm & 3 cm
"""

from microbit import *
from time import sleep


display.clear()
sleep(1)

display.scroll("A rectangle has dimensions 5 cm & 3 cm.")
display.clear()
sleep(1)
display.scroll("The perimeter would be: " + str(2 * (5 + 3)))
display.clear()
sleep(1)
display.scroll("The area would be: " + str(5 * 3))
