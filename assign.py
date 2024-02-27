#concatinate

d1  = {1:2}
d2 = {2:3}
d3 = {3:4}
d4 = {}
t = (d1,d2,d3)
for i in t:
    d4.update(i)
print(d4)    

#