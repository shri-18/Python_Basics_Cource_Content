# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:33:37 2023

@author: shrik
"""

"""
write a code for calculate the price of order bill:
    1. small = $15
    2. mediun = $20
    3.mediun = $25
    
    if yo want to add peproni for 
    1.small = $2
    2. mediun and Large = $3
    
    extra chees =  $1
    
"""

print("--+++ Welcome TO Dominos +++--")    

n = input("Enter Your order :: ")
bill = 0
m = n.split(' ')

if 'small' in m:
    bill = bill+15
    if 'preponi' in m:
        bill = bill+2
    if 'chees' in  m:
        bill = bill+1
        
elif 'medium' in m:
    bill = bill+ 20
    if 'preponi' in m:
        bill = bill+3  
    if 'chees' in  m:    
        bill = bill+1    

elif 'large' in m:
    bill = bill+ 25
    if 'preponi' in m:
        bill = bill+3  
    if 'chees' in  m:
        bill = bill+1      
        
print('Your Bill :: $',bill)        