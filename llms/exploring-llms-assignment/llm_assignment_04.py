#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 15:24:40 2025

@author: kalyani
"""
import logging
from transformers import pipeline
logging.getLogger("transformers").setLevel(logging.ERROR)

generic_prompt = "Write a story about a frog."
# prompt engineering to make it more detailed
steps_prompt = "Write a story about a frog in the following order: exposition, rising action, climax, falling action, resolution."
few_shot_prompt = "Write a story about a frog. Some narrative examples are: a frog encounters a witch in a forest that tries to steal its limbs. Or a frog is tasked with a dangerous journey in the forest to retrieve some gold coins."
roleplay_prompt = "Imagine you are an oral storyteller in a Kumeyaay village. Tell your children a story about a frog and include a lesson about bravery."

generator = pipeline('text-generation', model='gpt2', framework='pt')

generic_story = generator(generic_prompt, max_length=200,num_return_sequences=1,return_full_text=False)[0]['generated_text']
steps_story = generator(steps_prompt, max_length=200,num_return_sequences=1,return_full_text=False)[0]['generated_text']
few_shot_story = generator(few_shot_prompt, max_length=200,num_return_sequences=1,return_full_text=False)[0]['generated_text']
roleplay_story = generator(roleplay_prompt, max_length=200,num_return_sequences=1,return_full_text=False)[0]['generated_text']

print("\nGeneric Prompt Result\n")
print(generic_story)

print("\nChain of Thought Prompt Result\n")
print(steps_story)

print("\nFew-Shot Learning Prompt Result\n")
print(few_shot_story)

print("\nRoleplay Prompt Result\n")
print(roleplay_story)
