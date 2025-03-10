#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:16:22 2025

@author: kalyani
"""

og_list =  ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(og_list)
og_list.append('fig')
print(og_list)
og_list.remove('apple')
print(og_list)
og_list.reverse()
print(og_list)


og_dict = {"name":"Kalyani", "age":25, "city":"San Diego"}
og_dict.update({"favorite color": "green"})
og_dict["city"] = "Boston"
print("Keys: ", end = "")
for k in og_dict.keys():
    print(k,end=", ")
print("Values: ", end = "")
for k in og_dict.values():
    print(k,end=", ")


fav_things = ('Midsommar','Labyrinth','The Grapes of Wrath')
print(f"Favorite things: {fav_things}")
try:
    fav_things[1] = 'Parasite'
except:
    print("Oops! Tuples cannot be changed.")
    
print(f"Length of tuple: {len(fav_things)}")
