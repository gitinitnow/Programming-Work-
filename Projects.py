#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 23:17:48 2023

@author: marco
"""

#%% Projects 

#Receive three variables as input and then print all possible combinations of these 

import itertools

var1 = input("Give me a number: ")
var2 = input("Give me a number: ")
var3 = input("Give me a number: ")

permutations = itertools.permutations([var1, var2, var3])
permutations_list = list(permutations)
print(permutations_list)


