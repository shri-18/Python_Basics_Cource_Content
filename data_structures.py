# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:32:50 2023

@author: shrikant
"""
__________________________________________________________________________
'''#TUPLES'''

tup1 = (1,5,6,9)        #creating tuple

print(f'tup1[0]: {tup1[0]}')     #accesing elements of tuple
print(f'tup1[1]: {tup1[1]}')
print(f'tup1[2]: {tup1[2]}')
print(f'tup1[3]: {tup1[3]}')
__________________________________________________________________________

'''Tuples are used to store multiple items in single variable.
Tuples are Immutable that is they cant unchangeble'''
__________________________________________________________________________
''' Tuples can hold different data types'''

tup2 = (1,'john',True,-23.45)
print(tup2)
__________________________________________________________________________
'''Iterating over tuple'''

tup3 = ('apple', 'orange', 'plum', 'banana')

for x in tup3:
    print(x)
__________________________________________________________________________
#Tuple Related Function(Methods)

tup3 = ('apple', 'orange', 'plum', 'banana','apple')

print('Lenth of tuple :: ',len(tup3))       #len method                            

count = tup3.count('apple')                 #count method
print('no.of aplle :: ',count)

#find index of specific element in tuple
print('apple index :: ',tup3.index('apple')) 
__________________________________________________________________________
'''iterating elements of tuple'''

tup3 = ('apple', 'orange', 'plum', 'banana','apple')
if 'orange' in tup3:
    print('Orange is in this tuple !!')
__________________________________________________________________________
#Nested Tuples

t1 = (1,2,3,4) 
t2 = ('john','shri','demon','stifen')

t3 = (43,t1,t2,5.5)      #tuple inside tuple
print(t3)   
__________________________________________________________________________

'''-------------------------------LIST---------------------------------'''

lst = ['john','paul','george','ringo']    #creation of list
lst1 = [1,4,6,7]

lst3 = [4.4,34,lst,lst1,'demon',True]

print(lst3)
__________________________________________________________________________

#accesing Elements from list
#use index slicing
lst = ['john','paul','george','ringo']
print(lst[1])
print(lst[1:2])
print(lst[::-1])
print(lst[:2])
print(lst[::2])
__________________________________________________________________

#List Methods
lst = ['john','paul','george','ringo']

#append method
lst.append('shri')
print(lst)

#extend method
lst.extend(['dinesh','prathmesh','yash','sanket'])
print(lst)

#insert method
lst.insert(1, 'dhananjay')
print(lst)

#remove method
lst = ['once','upon','a','time']
lst.remove('upon')
print(lst)

#pop method (just like remove bt just have to pass index of element)
lst = ['shri', 'dinesh', 'prathmesh', 'yash', 'sanket']
lst.pop(3)
print(lst)


________________________________________________________________________
#concatinate 2 lists

l1 = [1,2,3]
l2 = [4,5,6]
l4 = ['shrikant','demon']
l3 = l1 + l2 + l4
print(l3)

_________________________________________________________________________
'''--------------------------- Set -----------------------------------'''
#creation of set 
 #it is use to remove the duplicate entities
 #it is Unordered thats why it sequence is changing
 
s = {'apple','banana','mango','pear','apple'}

print(s)      #it doesn't allow duplicates

#accessing element in set
s = {'apple','banana','mango','pear','apple'}
for i in s:
    print(i)

#methods of set
#adding items to set  .add method
s = {'apple','banana','mango','pear'}
s.add('orange')
print(s)

# update method (pass list to update)
s = {'apple','banana','mango','pear'}
s.update(['dragon','blue spider lily'])
print(s)

# .remove and .discard method
s = {'apple','banana','mango','pear','apple'}
s.remove('apple')
s.discard('pear')
print(s)
_________________________________________________________________________
'''--------------------------- Set Operations ------------------------'''
#unioin ,intersection, difference


s1 = {'apple','orange','banana'}
s2 = {'grapes','lime','banana'}

print('Unioin ::', s1 | s2)
print('Intersection :: ', s1 & s2)
print('Difference:: ', s1 - s2)  #it gives element present set 1 but not                     
                                 #in set 2
_________________________________________________________________________
'''--------------------------- Dictionary ---------------------------'''
#dictinary dont allow duplicates
#cretion dictionary

capitals = {
            'Maharashtra': 'Mumbai',
            'Gujrat': 'Ahmdabad',
            'UP': 'Lacknow',
            'Karnataka' : 'Banglore',
            'Andhrapraddesh': 'Hydrabad'
            }

print(capitals)

#keys

dict1 = {
        'Brand':'Ford',
        'Model':'Mustang GT',
        'year':2021,
        'year':2020
        }
print(dict1)
_________________________________________________________________________
#accesing element

capitals = {
            'Maharashtra': 'Mumbai',
            'Gujrat': 'Ahmdabad',
            'UP': 'Lacknow',
            'Karnataka' : 'Banglore',
            'Andhrapraddesh': 'Hydrabad'
            }
print("capital of Maharashtra:: ",capitals['Maharashtra'])
_________________________________________________________________________
#adding new entry

capitals = {
            'Maharashtra': 'Mumbai',
            'Gujrat': 'Ahmdabad',
            'UP': 'Lacknow',
            'Karnataka' : 'Banglore',
            'Andhrapraddesh': 'Hydrabad'
            }

capitals['west bangol'] = 'Kolkata'
print(capitals)
_________________________________________________________________________
#changing key Value

capitals = {
            'Maharashtra': 'Mumbai',
            'Gujrat': 'Ahmdabad',
            'UP': 'Lacknow',
            'Karnataka' : 'Banglore',
            'Andhrapraddesh': 'Hydrabad',
            'west bangol': 'Kolkata'
            }

capitals['Gujrat'] = 'Gandhinagar'
print(capitals)

_________________________________________________________________________
#removing from entity
#pop method
capitals = {
            'Maharashtra': 'Mumbai',
            'Gujrat': 'Gandhinagar',
            'UP': 'Lacknow',
            'Karnataka' : 'Banglore',
            'Andhrapraddesh': 'Hydrabad',
            'west bangol': 'Kolkata'
            }

capitals.pop('Karnataka')
print(capitals)

#del method
del capitals['UP']

print(capitals)
_________________________________________________________________________
#iterating over keys

capitals = {
            'Maharashtra': 'Mumbai',
            'Gujrat': 'Gandhinagar',
            'UP': 'Lacknow',
            'Karnataka' : 'Banglore',
            'Andhrapraddesh': 'Hydrabad',
            'west bangol': 'Kolkata'
            }
print('States ::' ,end= ' ')
for states in capitals:
    print(states, end=', ')                    #iterating keys
    
print('\n')

print('Capitals ::', end=' ')    
for states in capitals:
    print(capitals[states], end= ', ')          #iterating values
_________________________________________________________________________
#keys , values and items
capitals = {
            'Maharashtra': 'Mumbai',
            'Gujrat': 'Gandhinagar',
            'UP': 'Lacknow',
            'Karnataka' : 'Banglore',
            'Andhrapraddesh': 'Hydrabad',
            'west bangol': 'Kolkata'
            }
print((capitals.values()))
print(capitals.keys())
print(capitals.items())
_________________________________________________________________________
#Checking Key membership
print('Karnataka' in capitals)
print('Bihaar'not in capitals)
_________________________________________________________________________
#dictionary can take values in tuples

season = {'summer':('march','april','may','June'),
'rainy': ('july','august','september','octomber'),
'winter': ('November','December','January','February')
          }

print(season['rainy'])
print(season['rainy'][0])
_________________________________________________________________________
#dictionary Methods
capitals = {
            'Maharashtra': 'Mumbai',
            'Gujrat': 'Gandhinagar',
            'UP': 'Lacknow',
            'Karnataka' : 'Banglore',
            'Andhrapraddesh': 'Hydrabad',
            'west bangol': 'Kolkata'
            }

#get method (it gives the value of key that passed)
print(capitals.get('UP'))
