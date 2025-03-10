#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 12:03:59 2025

@author: kalyani
"""
import sys
welcome_msg = "\nWelcome to the Error-Free Calculator! Choose an operation: 1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Exit \n"

opdict = {1: "+", 2: "-", 3: "x", 4: "/"}
try:
    op = int(input(welcome_msg))
    if op not in [1,2,3,4,5]:
        print("\nMust be valid number between 1 and 5")
        sys.exit()
except ValueError:
    print("\nMust be valid number between 1 and 5")
    sys.exit()
    
if op == 5:
    sys.exit()
try:
    n1 = float(input("\nEnter the first number: "))
    n2 = float(input("\nEnter the second number: "))
except ValueError:
    print("\nMust be valid number")
    sys.exit()

opc = opdict[op]

if op == 1:
    t = n1+n2
elif op == 2:
    t = n1-n2
elif op == 3: 
    t = n1*n2
elif op == 4:
    try:
        t = n1/n2
    except ZeroDivisionError:
        print("\nOops! Division by zero is not allowed")
        sys.exit()
        
print(f"{n1}{opc}{n2}={t}")
