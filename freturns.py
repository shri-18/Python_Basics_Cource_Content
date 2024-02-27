# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 09:23:15 2023

@author: shrik
"""

_________________________________________________________________________
#return dictionary

def dict(n,m):
    return {n:m}

dict('name', 'Shrikant')
__________________________________________________________________________#list return

def lis(n,m,o):
    return [n,m,o]

lis(1, 2, 3)
__________________________________________________________________________
#Passing Arbitrary Number of argument

def pizza(*toppings):
    print(toppings)
    
pizza('preponi','chees','sauce')
__________________________________________________________________________
#same with loop output
def pizza(*toppings):
    print("making pizza with following toppings ::")
    
    for toppings in toppings:
        print(f'- {toppings}')
    
pizza('preponi','chees','sauce')
__________________________________________________________________________
#passinf Arguments with 

def pizza(size,*toppings):
    print(f"making pizza of {size} inches with following toppings :: ")
    
    for toppings in toppings:
        print(f'- {toppings}')
    
pizza(34, 'preponi','chees','sauce')
__________________________________________________________________________
#creating module and use that 
import pizza
pizza.pizza(34.'preponi','chees')
__________________________________________________________________________
#importing specific function from your created module

from pizza import pizza as make_pizza

make_pizza(34,'preponi','chees')
__________________________________________________________________________


                        





























