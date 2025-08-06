import math


def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True
    

def is_pernocius():
    for k in range(222281, 222381):
        bin_list = list(bin(k))
        sum = 0
        for i in range(2,len(bin_list)):
            sum += int(bin_list[i] )
        if is_prime(sum):
            print(k)

is_pernocius()