# n = int(input('Enter the Range :: '))
# for i in range(n):
#     print(i+1)

n = int(input("Enter the number to stop :: "))
for  i in range(0,16):
    if i == n:
        break
    if i != n:
        continue
    
    print(i)
print('Stop is Successful')

#anonymous Variable

for _ in range(10):
    print('.',end='')
    # print('.',end='\n')
    
    #print()    
    
l = [1,2,3,4]
n = len(l)
for i in range(0,n):
    print(l[i])
    
#step 

for i in range(2,10+1,2):
    print(i)    
    
    
for i in range(n):
    for j in range(i):
        print("*")    