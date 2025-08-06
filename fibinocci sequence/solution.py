def fibonacci(num):
    list = []
    
    for i in range(num):
        if len(list)==0 or len(list)==1:
            list.append(1)
        else:
            firstNum = list[i-1]
            secondNum = list[i-2]
            list.append(firstNum+secondNum)
            
    return list
        