#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:44:48 2025

@author: kalyani
"""

s = "Python is amazing!"
print(f"First word: {s[:7]}")
print(f"Amazing part: {s[10:17]}")
print(f"Reversed string: {s[::-1]}")


s = " hello, python world! "
print(s)
s = s.strip()
print(s)
s = s.capitalize()
print(s)
s = s.replace("world", "universe")
print(s)
s = s.upper()
print(s)


s = input("Enter a word: ")
rs = s[::-1]
if rs == s:
    print(f"Yes, \'{s}\' is a palindrome!")
else:
    print(f"No, \'{s}\' is not a palindrome!")
