#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:28:10 2020

@author: AnnieGomez
"""

# Getting user inputs
x = int(input("Choose 1 to convert from Fahrenheit to Celsius; Choose 2 to convert from Celsius to Fahrenheit: "))

# to convert from Fahrenheit to Celsius
if x == 1:
    # Get temperature in Fahrenheit from user
    f = float(input("Enter the temperature in Fahrenheit: "))
    c = (f-32)*5/9
    c = float(c)
    print("Temperature in Celsius: {}".format(c))
    
# to convert from Celsius to Fahrenheit
if x == 2:
    # Get temperature in Celsius from user
    c = float(input("Enter the temperature in c: "))
    f = c/5*9+32
    f = float(f)
    print("Temperature in Fahrenheit: {}".format(f))

exit()