#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:15:36 2020

@author: clarekirkland
"""

import string
alphabet = string.ascii_lowercase

# Decypher the user's cyper by mapping to the alphabet
def decypher(code):
    graph = []
    count = 1
    for i in code:
        if (i.isalpha()):
            i = i.lower()
        if (i not in graph):
            graph.append(i)
        else:
            graph.append(str(count))
            count = (count + 1)%10
    return graph


# Decode the encoded text based on the map
def decode(encoded,c_map):
    ans = ""
    for i in encoded:
        if (i.isalpha()):
            i = i.lower()
        if (i in c_map):
            ans += alphabet[c_map.index(i)]
        else:
            ans += ' '
    return ans
    
# Get and translate cypher 
code = str(input("What is the encryption code? "))
c_map = decypher((code.replace(' ','')).lower())
    
# Loop over the user's encoded text
while (True):
    res = input("What do you want to decode? ")
    print(decode(res, c_map))
