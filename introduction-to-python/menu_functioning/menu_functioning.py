#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 15:09:11 2025

@author: kalyani
"""
import sys
import turtle

def fibonacci(n):
    if n < 1:
        return("number should be positive")
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def factorial(n):
    if n < 0:
        return("number should be non-negative")
    if n == 0:
        return(1)
    else:
        return n*factorial(n-1)
def fractal(length, depth):
    if depth == 0:
        return
    for _ in range(3):
        turtle.forward(length)
        fractal(length / 2, depth - 1)
        turtle.left(120)


welcome_msg = "Welcome to the Recursive Artistry Program! Choose an option: 1. Calculate Factorial 2. Find Fibonacci 3. Draw a Recursive Fractal 4. Exit\n"

try:
    i = int(input(welcome_msg))
except ValueError:
    print("Enter a valid number")
if i not in [1,2,3,4]:
    print("Enter a number between 1 and 4")
    sys.exit()

if i == 1:
    n = int(input("Enter a number to find its factorial: "))
    print(f"The factorial of {n} is {factorial(n)}")
elif i == 2:
    n = int(input("Enter the position of the Fibonacci number: "))
    print(f"The number {n} Fibonacci number is {fibonacci(n)}")
elif i == 3:
    turtle.speed(0)
    fractal(200, 3)
    turtle.done()
else:
    sys.exit()
