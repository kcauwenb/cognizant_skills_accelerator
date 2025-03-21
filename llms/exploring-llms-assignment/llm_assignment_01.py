#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:29:47 2025

@author: kalyani
"""
from transformers import AutoTokenizer
from transformers import AutoModel
import torch
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# task 1
# bee movie script
text = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little. Barry! Breakfast is ready! Coming! Hang on a second. Hello? - Barry? - Adam? - Can you believe this is happening? - I can't. I'll pick you up. Looking sharp. Use the stairs. Your father paid good money for those. Sorry. I'm excited. Here's the graduate. We're very proud of you, son. A perfect report card, all B's. Very proud. Ma! I got a thing going here. Ah, you got some lint on your fuzz. Ow! That's me! Wave to us! We'll be in row 118,000. Bye! Barry, I told you, stop flying in the house! Hey, Adam. - Hey, Barry. - Is that fuzz gel? - A little. Special day, graduation. Never thought I'd make it. Three days' grade school, three days high school. Those were awkward. Three days college. I'm glad I took a day off in the middle to hitchhike around the hive."

# task 2
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

# task 3
# count tokens
print("Tokens:", tokens)
print("Number of tokens:", len(tokens))

# task 4
# extract embeddings
model = AutoModel.from_pretrained("bert-base-uncased")
input_ids = tokenizer.encode(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(input_ids)
    embeddings = outputs.last_hidden_state.squeeze(0)  # Shape: (num_tokens, embedding_dim)
print("Embedding shape:", embeddings.shape)  # Example: (number of tokens, 768)

# plot embeddings with pca
pca = PCA(n_components=2)
embeddings_2d = pca.fit_transform(embeddings.numpy())
plt.figure(figsize=(8, 6))
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], color='blue')
for i, token in enumerate(tokens[: len(embeddings_2d)]):
    plt.text(embeddings_2d[i, 0], embeddings_2d[i, 1], token, fontsize=12)
plt.title("Token Embeddings Visualized with PCA")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.show()



