def list_pretty_print(items):
    count=1
    for item in items:
        if(count!=5):
            print(item,end =", ")
        else:
            print(item)
            count=0
        count+=1 