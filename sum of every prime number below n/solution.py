import math

def is_prime(n):
    if n ==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    else:
        return True

def sum_primes(num):
    total = 0
    for i in range(num):
        if is_prime(i):
            total += i
    
    return total

print(sum_primes(2))