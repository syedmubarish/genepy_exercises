for i in range(0,1001):
    digitList = list(str(i))
    digitSum = 0
    for j in digitList:
        digitSum += int(j)
    
    if i%7==0 and digitSum%3==0:
        print(i)