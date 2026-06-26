#loops

for i in [1,2,3,4,5]:
    print(i)

for z in "broadway":
    print(z)



a={
"name":"hari",
"address":"nepal"
}

for i in a:
    print(a)


for i in a.values():
    print(i)

for i in a:
    print(i, a[i])

for i in range(20,1,-1):
    print(i)

print("_________"*10)    

for i in range(1,11,1):
    print(f' 7 X {i} = {7*i}')


# break, continue 

for i in range(1,11,1):
    if i==7:                                        # continue replays the loop back without going any further
        continue
    print(f' 7 X {i} = {7*i}')

for i in range(1,11,1):
    if i==7 or i==8:                                        # break stops the loop itself 
        break
    print(f' 7 X {i} = {7*i}')
    print('\n')

a = {10,20,10,10}
for i in a:
    for j in range(1,11,1):
        print(f' {i} x {j} = {i*j}')
    print('\n')
    
          
result = [] 
for i in range(1,5):
    data = int(input(f"Enter the {i} number "))  
    result.append(data)

for i in set(result):
    for j in range(1,11,1):
        print(f'{i} x {j} = {i*j}')


# a=[]    empty list
# a=()    empty tuple
# a={}    empty dictonary
# a=set() empty set




#while loop

i = 1
while(i<=10):
    print(f'{i}')
    i = i+1
