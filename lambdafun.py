# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:13:19 2023

@author: shrik
"""
__________________________________________________________________________
#lambda function / anonymous function

def add(a,b,c):
    sum1 = a+b+c
    return sum1
print(add(4,5,6))

add = lambda a,b,c : a+b+c

add(4,5,6)
__________________________________________________________________________
#
mul = lambda x,b,m : x*b*m
mul(5,8,9)
__________________________________________________________________________
#
add = lambda *arg : sum(arg)

add(1,4,6,2,5,36,6,4,6)
__________________________________________________________________________

#key word agrgument
def person(name,**data):
    print(name)
    print(data)

person(name= 'navin', age= ' 18',place= 'mumbai', mob_no=8459886930) 
__________________________________________________________________________

''' **kwargs in function definition in python is used to pass a keyword,
variable-lengtharguments list. We use the name kwargs with the double star.
the reasonis that th double star allows us to pass through keyword arguments
(and any number of them)'''
__________________________________________________________________________

#how to use the dict elements as arg

def person(name , **data):
    print(name)
    for i,j in data.items():
        print(i+' = '+str(j))
        
person('Navin', age= '18',place= 'mumbai', mob_no=8459886930)     
__________________________________________________________________________

#dictionary methods
val = lambda **data : sum(data.values())
print(val(a=2,b=5,c=9,f=5))
__________________________________________________________________________

#if cond in lambda func
max = lambda a,b: a if(a>b) else b
print(max(2,6))
__________________________________________________________________________









____________