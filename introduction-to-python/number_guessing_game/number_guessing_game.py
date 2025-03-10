#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 10:35:03 2025

@author: kalyani
"""
import random
import sys
number_to_guess = random.randint(1, 100)
guess_counter = 1

while guess_counter < 11:
    guess = int(input("Guess the number (between 1 and 100): "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {guess_counter} attempts!")
        sys.exit()
    guess_counter += 1
print("Game over! Better luck next time!")