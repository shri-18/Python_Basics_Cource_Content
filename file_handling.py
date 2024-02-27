#File Handling

with open ('pi_digits.txt') as file_object:
    contents  = file_object.read()
print(contents)  

# f = open('pi_digits.txt','r')
# print(f)  
*******************************************************************************************

with open ('pi_digits.txt') as file_object:
    contents  = file_object.read()
print(contents.rstrip())
  
*******************************************************************************************

file_path = 'C:/1-python/Day 5 (File Handling)/pi_digits.txt'
with open (file_path) as filex:
    content = filex.read()
print(content.rstrip())   
 
*******************************************************************************************


file_name = 'C:/1-python/Day 5 (File Handling)/pi_digits.txt'
with open(file_name)as file_object:
    for line in file_object:
        print(line)
        
*******************************************************************************************


file_name = 'C:/1-python/Day 5 (File Handling)/pi_digits.txt'
with open(file_name)as file_object:
    lines = file_object.readlines()
    pi_strings = ''
    for line in lines:
        pi_strings += line.rstrip()
        print(pi_strings)
        print(len(pi_strings))
        
*******************************************************************************************

filen = 'programming.txt'
with open(filen, 'w')as file_obj:
    file_obj.write('I love Python')

*******************************************************************************************


filen = 'programming.txt'
with open(filen, 'w')as file_obj:
    file_obj.write('I love Python')        

*******************************************************************************************
#append mode
filen = 'programming.txt'
with open(filen, 'a')as file_obj:
    file_obj.write(' I love all the snecks')  
    

*******************************************************************************************

    