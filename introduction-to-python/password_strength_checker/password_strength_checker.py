#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 10:43:52 2025

@author: kalyani
"""
#one uppercase letter, one lowercase letter, one digit, and one special character
chardict = {"uppercase letter":False,"lowercase letter":False,"digit":False,"special character":False}

pw = input("Enter a password: ")
for c in pw:
    if c.isupper(): chardict["uppercase letter"] = True
    if c.islower(): chardict["lowercase letter"] = True
    if c.isdigit(): chardict["digit"] = True
    if not c.isalnum(): chardict["special character"] = True
lacking = [k for k, v in chardict.items() if v == False]
if len(lacking) == 0:
    print("Your password is strong!")
else:
    l2 = (" and one ").join(lacking)
    print(f"Your password needs at least one {l2}.")
