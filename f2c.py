#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 18:59:25 2020

@author: AnnieGomez
"""

# Initializing variables
f=0
c=0

f = input ("Enter the temperature in Farenheit: ")
f = int(f)
c = (f-32)*5/9
c = int(c)
print("Temperature in Celsius: {}".format(c))