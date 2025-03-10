#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:34:59 2025

@author: kalyani
"""
try:
    n = int(input("Enter a number: "))
    print(f"100 divided by {n} is {100/n}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
    




n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
try:
    n=n1/n2
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
finally:
    print("This block always executes")



