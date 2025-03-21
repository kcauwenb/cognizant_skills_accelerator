#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 14:49:16 2025

@author: kalyani
"""
import logging
from transformers import pipeline
import sys

logging.getLogger("transformers").setLevel(logging.ERROR)

generator = pipeline('text-generation', model='gpt2', framework='pt')

def chat():
    print("Chatbot: Hello user! Ask me anything! or type 'exit' to end the conversation.")
    while True:
        prompt = input("You: ")
        if prompt.lower() == 'exit':
            print("Chatbot: Goodbye!")
            sys.exit()
        response = generator(prompt, max_length=100,num_return_sequences=1,return_full_text=False)[0]['generated_text']
        print("Chatbot:", response)

chat()
