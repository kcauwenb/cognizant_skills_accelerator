#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 11:27:16 2025

@author: kalyani
"""
import logging
from transformers import pipeline
logging.getLogger("transformers").setLevel(logging.ERROR)

generic_prompt = "Write a story about a frog."
detailed_prompt = "Write a fantasy story about a frog who encounters an unfriendly witch"
specific_prompt = "Write a fantasy story about a spotted frog who encounters a witch that makes fun of it for having acne. Describe the frog's rebuttal. Keep it to less than 200 words."
generator = pipeline('text-generation', model='gpt2', framework='pt')
generic_story = generator(generic_prompt, max_length=200,num_return_sequences=1,return_full_text=False)[0]['generated_text']
detailed_story = generator(detailed_prompt, max_length=200,num_return_sequences=1,return_full_text=False)[0]['generated_text']
specific_story = generator(specific_prompt, max_length=200,num_return_sequences=1,return_full_text=False)[0]['generated_text']

print("\nGeneric Prompt Result\n")
print(generic_story)

print("\nDetailed Prompt Result\n")
print(detailed_story)

print("\nHighly Specific Prompt Result\n")
print(specific_story)

# the highly specific prompt was followed the best. But all prompts were not followed well because the emphasis was on the story aspect not the frog aspect, so a lot of the writing was about writing itself.

