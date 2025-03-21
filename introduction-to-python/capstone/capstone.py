#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 11:22:51 2025

@author: kalyani
"""
import sys
t_list = []
s_dict = {}
print("\nWelcome to the Study Manager!")
recurring_message = "\nWelcome to the Study Manager!\nEnter a number to:\n1: add task\n2: track tasks\n3: add score\n4: track scores\n5: exit\n"

# add task
def opt1():
    try:
        t = input("\nEnter task: " )
        d = input("\nEnter deadline (YYYY/MM/DD): ")
        p = int(input("\nEnter priority (1 highest 10 lowest): "))
        if p in range(1,11):
            t_list.append({"t":t, "d":d, "p":p})
        else:
            print("\nPlease enter a number between 1 and 10")
    except ValueError:
        print("\nPlease enter a number between 1 and 10")
    return
# track tasks
def opt2():
    if not t_list:
        print("\nNo tasks")
        return
    else:
        sorted_t_list = sorted(t_list, key = lambda x: (x["p"],x["d"]))
        print("\nTasks by priority and deadline:")
        for task in sorted_t_list:
            print(f"\n{task['t']} (Priority: {task['p']}, Deadline: {task['d']})")
    return
# add score
def opt3():
    try:
        s = input("\nEnter subject name: ")
        g = float(input(f"\nEnter grade (0-100): "))
        if g < 0 or g > 100:
            raise ValueError("\nScore must be between 0 and 100.")
        s_dict[g] = s
    except ValueError as e:
        print(f"\nGrade must be a number between 0 and 100")
    return
# track scores
def opt4():
    if not s_dict:
        print("\nNo grades")
        return
    else:
        scores = list(s_dict.keys())
        for sc in scores:
            print(f"\nSubject: {s_dict[sc]}, Grade: {sc}")
        w = s_dict[min(scores)]
        a = sum(scores)/len(scores)
        print(f"\nWeakest area: {w}")
        print(f"\nAvg grade: {a}")
    return


while(True):
    try:
        f = int(input(recurring_message))
        if f == 1:
            opt1()
        elif f == 2:
            opt2()
        elif f == 3:
            opt3()
        elif f == 4:
            opt4()
        elif f == 5:
            sys.exit()
        else:
            print("\nPlease enter a number between 1 and 5")
    except ValueError:
            print("\nPlease enter a number between 1 and 5")








