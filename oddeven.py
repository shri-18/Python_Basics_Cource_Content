start, end = input().split()

print(':: Odd Number :: ')
for i in range(int(start), int(end)+1) :
    if i % 2 != 0:
        print(f'{i}')
    else:
        continue
    
print(':: Even Number :: ')
    
for i in range(int(start), int(end)+1) :
    if i % 2 == 0:
        print(f'{i}')
    else:
        continue    
           