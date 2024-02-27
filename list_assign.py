# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:02:19 2023

@author: shrik
"""

#write python programm to add all the aitem in list

____________________________________________________________________
'''-------------------- List Assignment ------------------------'''
def summ(l):
    s = 0
    for i in l:
        s = s+i
    return(s)    
l = [1,6,5,6,7,3,5,]
print(summ(l))
print(sum(l))             #built in method for sum
____________________________________________________________________
#mutiply all the items in list

def mul(l):
    x = 1
    for i in l:
        x = x*i
    return x

l = [1,6,5,6,7,3,5,]
print(mul(l))    
___________________________________________________________________
#find largest and smallest number in list
l = [1,6,5,6,7,3,5,]
print(max(l))
print(min(l))

l.sort()
#print(l)
print(l[::-1][0])
print(l[0])
___________________________________________________________________
#python programm to count the no of string which satisfies the 
# condition that ths string length is 2 or more and the 1st amd last 
# charecter should be same from given list string

l1 = ['abc','xyz','aba','1211'] 
c= 0
for i in l1:
    m = i.split()
    if len(i)>=2:
        if i[0] == i[-1]:
            c+=1
print('Number of string that satisfies conditions are :: ',c)     ___________________________________________________________________
#write a python priogramm to get list soted in increasing order 
# by the last element of the tuples in such way that your 
# last element in inreasing order

l = [(2,5),(1,2),(4,4),(2,3),(2,1)]
l1 = []
l2 = []
l3 = []
for i in l:
    l1.append(i[1])
l1.sort()
for i in l:
    for j in range(len(l1)):
        if i[1] == l1[j]:
            l2.append(j)
            
for i in l2:
    l3.append(l[i])
print(l3)                
___________________________________________________________________
'''Write programm to remove duplicates from given list'''
l = [10,20,30,20,10,50,60,40,80,50,40]
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)  

a = list(set(l))
print(a)
___________________________________________________________________
# program  to copy list

l = [ 10,20,4,50,50] 
print('l :: ',end='') 
print(l)    
x = l
print('x :: ',end='') 
print(x)
___________________________________________________________________
#program to find the list of words that are longer than n from given 
# list of words


def long_word(n,str):
    l = str.split(' ')
    m = []
    for i in l:
        if len(i) > n:
            m.append(i)
    return m     

st = 'the quick brown fox jumps over the lazy dog'   
print(long_word(3,st))        
___________________________________________________________________
#Write function that takes 2 list and gives the common element from those

def common(l1,l2):
    for i in l1:
        if i in l2:
            return True
    return False

print(common([1,2,3,4,5],[5,6,7,8,9]))    
___________________________________________________________________
#Difference between 2 lists
l1 = [1,2,3,4]
l2 = [2,4,7,9,5]
d1 = list(set(l1)-set(l2))
d2 = list(set(l2)-set(l1))
print(d1+d2)

#OR

def diff(l1,l2):
    x = []
    y = []
    for i in l1:
        if i not in l2:
            x.append(i)
    for i in l2:
        if i not in l1:
            y.append(i)            
    return(x+y) 
l1 = [1,2,3,4]
l2 = [2,4,7,9,5]
 
print(diff(l1,l2))    
___________________________________________________________________
#convert list in string
l = ['s','h','r','i']
st = "".join(l)
print(st)
___________________________________________________________________
#find the of an item in list
l = [1,2,3,4,5]
print(l.index(4))