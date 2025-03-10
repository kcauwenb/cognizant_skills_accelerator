#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:55:21 2025

@author: kalyani
"""

age = int(input("How old are you? "))
if age > 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    X = 18 - age
    print(f"Oops! You’re not eligible yet. But hey, only {X} more years to go!")