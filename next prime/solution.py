from itertools import count
from math import sqrt
import sys


for i in count(start = 100000000, step = 1):
    for j in range(2,int(sqrt(i)+1)):
        if i%j==0:
            break
    else:
        print(i)
        sys.exit()