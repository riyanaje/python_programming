#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:28:10 2020

@author: AnnieGomez
"""

# Initializing varibles
x=0
x = input ("Choose 1 to convert from Farenheit to Celsuis; Choose 2 to convert from Celsius to Farenheit: ")
x = int(x)

# to convert from Farenheit to Celsius
if (x==1):
    # Initializing varibles 
    f=0
    c=0
    f = input ("Enter the temperature in Farenheit: ")
    f = int(f)
    c = (f-32)*5/9
    c = int(c)
    print("Temperature in Celsius: {}".format(c))
    
# to convert from Celsuis to Farenheit 
if (x==2):
    # Initializing variables
    f=0
    c=0
    c = input ("Enter the temperature in Celsuis: ")
    c = int(c)
    f = c/5*9+32
    f = int(f)
    print("Temperature in Farenheit: {}".format(f))