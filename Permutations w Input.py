#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 23:17:48 2023

@author: marco
"""

#%% Projects 

#Receive three variables as input and then print all possible combinations of these 

import itertools #in order to use the .permutations() later on

var1 = input("Give me a number: ") #first variable received from user 
var2 = input("Give me a number: ") #second variable received from user
var3 = input("Give me a number: ") #third variable received from user 

permutations = itertools.permutations([var1, var2, var3]) #.permutations() gets all possible permutations of var1-var3 (which are stored in a list) 
permutations_list = list(permutations) #permutations above are stored in a list called 'permutations_list'
print(permutations_list) #prints the list 


