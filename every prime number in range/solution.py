import math
primes = []
for i in range(10000,10051):
    for j in range(2,int(math.sqrt(i))):
        if i % j == 0:
            break
    else:
        primes.append(i)
  
index = 0      
for i in primes:
    if index != len(primes)-1:
        print(i,end=", ")
    else:
        print(i)
    index+=1