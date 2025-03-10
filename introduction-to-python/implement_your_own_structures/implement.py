#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 11:22:51 2025

@author: kalyani
"""
import sys
inventory = {}
print("\nWelcome to the Inventory Manager!")


while(True):
    f = input("\nEnter 'add' to add a new item, 'remove' to remove an item, 'update' to update an item', 'check' to see the inventory, 'calculate' to calculate the total value, or 'exit' to exit: ")
    if f == 'add':
        item = input("Item (string): ")
        quantity = input("Quantity (int): ")
        price = input("Price (float): ")
        inventory[item] = (quantity,price)
    elif f == 'remove':
        items = ' '.join(inventory.keys())
        item = input(f"Pick an item to remove: {items}\n")
        try:
            del inventory[item]
        except KeyError:
            print(f"{item} is not in the inventory")
    elif f == 'update':
        items = ' '.join(inventory.keys())
        item = input(f"Pick an item to update: {items}\n")
        quantity = input("Quantity (int): ")
        price = input("Price (float): ")
        try:
            inventory[item] = (quantity,price)
        except KeyError:
            print(f"{item} is not in the inventory\n")
    elif f == 'calculate':
        total = 0
        if len(inventory.keys()) != 0:
            for k in inventory.keys():
                total += float(inventory[k][0])*float(inventory[k][1])
        print(f"\nTotal price of inventory: ${total}")
    elif f == 'check':
        print(inventory)
    else:
        sys.exit()








