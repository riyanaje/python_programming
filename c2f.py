#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:20:20 2020

@author: AnnieGomez
"""

# Initializing varibles
f=0
c=0

c = input ("Enter the temperature in Celsius: ")
c = int(c)
f = c/5*9+32
f = int(f)
print("Temperature in Farenheit: {}".format(f))
