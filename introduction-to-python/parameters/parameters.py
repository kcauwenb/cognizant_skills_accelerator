#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 13:19:44 2025

@author: kalyani
"""

# task 1
def greet_user(name):
    print(f"Hello hello {name}!")
def add_numbers(n1,n2):
    print(f"The sum of {n1} and {n2} is {n1+n2}.")
    
greet_user("Bob")
add_numbers(1,2)

# task 2
def describe_pet(pet_name:str,animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")
describe_pet("felix","cat")
describe_pet("ink")

# task 3
def make_sandwich(*args):
    ilist = ' '.join(args)
    print("Making a sandwich with the following ingredients:", ilist)
make_sandwich("Lettuce","Tomato","Cheese")

# task 4
def factorial(n):
    if n < 0:
        return("number should be non-negative")
    if n == 0:
        return(1)
    else:
        return n*factorial(n-1)
n=5
print(f"The factorial of {n} is {factorial(n)}")

def fibonacci(n):
    if n < 1:
        return("number should be positive")
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=6
print(f"The number {n} Fibonacci number is {fibonacci(n)}")

