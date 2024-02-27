#JSON =  JavaScript Object Notation
# from json import dump
import json
numbers = [1,2,3,4,5]
file_name = 'num.json'
with open(file_name,'w') as fil:
    x = json.dump(numbers,fil)
print(x)

_______________________________________________

d = {0:10,1:20}
print(d)
d.update({2:30})
print(d)