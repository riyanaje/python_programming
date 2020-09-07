#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:57:07 2020

@author: AnnieGomez
"""

# Getting user inputs
x = int(input("Choose 1 to convert from Fahrenheit to Celsius; Choose 2 to convert from Celsius to Fahrenheit: "))

# to convert from Fahrenheit to Celsius
def f2c():
    # Get temperature in Fahrenheit from user
    f = float(input("Enter the temperature in Fahrenheit: "))
    c = (f-32)*5/9
    c = float(c)
    return c

# to convert from Celsius to Fahrenheit
def c2f():
    # Get temperature in Celsius from user
    c = float(input("Enter the temperature in c: "))
    f = c/5*9+32
    f = float(f)
    return f

if x == 1:
    v = f2c()
    v = round(v, 2)
    print("The temperature in Celsius is: {}".format(v))
if x == 2:
    v = c2f()
    v = round (v, 2)
    print("The temperature in Fahrenheit is: {}".format(v))

exit()
