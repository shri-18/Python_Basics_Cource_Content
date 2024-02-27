# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 14:56:06 2023

@author: shrikant
"""


____________________________________________________________________________________________________________________________________________
#Pass Generate 

import random
import string

l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
m = []
for i in range(8):
    x = random.choice(l)
    m.append(x)    
r = random.choice(string.punctuation)    
m.append(r)

k = random.randrange(1,100)

m.append(str(k))
d = ''    
z = d.join(m)
print("Generated Password :: ",z)


__________________________________________________________________________
#Check Paa Strength

p = 'Shrikant@77'

n = len(p)
c= 0
d = 0
if n >= 8:
    for i in range(n):
        a = p[i]
        if a.islower():
            c+=1
              
        elif a.isupper():
            d+=1
       
if c >= 1 and d >= 1:
    print("Password is strong !")
else:
    print("Password is Weak !")
  
__________________________________________________________________________     
        
