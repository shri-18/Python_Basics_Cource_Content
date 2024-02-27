# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:16:47 2023

@author: shrikant 
"""



#function for prime number 
def prime(n):
    c = 1
    for i in range(2,n):
        if n%i == 0:
            c+=1
    if c > 1:
        print(f"{n} is not a prime number")
    else : 
        print(f"{n} is a prime number")    
        
prime(8)        

##############################################################################
''' function with no argument'''

def my_name():
    print("Shrikant Machindra Ilhe")

my_name()    

###############################################################################

'''passing argument and used as logic of function'''

def funk(n):
    print('This is the Username : ',n)

funk('Sanjivani')

##############################################################################
'''positional Argumenent'''

def pet(pet_type,name):
    print('Animal :: ',pet_type)
    print("Name :: ",name)

pet('dog','tuffy')     #order matters iin position argument

##############################################################################
'''default values in function '''

def animal(brid,an_type='DOG'):
    print(f"{brid} {an_type}")

animal("HUSKY")

##############################################################################
'''



