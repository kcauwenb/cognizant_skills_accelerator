#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:13:06 2025

@author: kalyani
"""

n = int(input("Enter the starting number: "))
while n > 0:
    print(str(n)+" ",end="")
    n-=1
print("Blast off!")

n = int(input("Enter a number: "))
for i in range(10):
    s = f"{str(n)} x {str(i+1)} = {str(n*(i+1))}"
    print(s+" ",end="")

n = int(input("Enter a number: "))
p = n
for i in range((n-1), 1, -1):
    p *= i
s = f"The factorial of {n} is {p}."
print(s+" ",end="")

