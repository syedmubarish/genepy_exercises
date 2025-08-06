def select_student(students, threshold):
    accepted = []
    refused = []
    res = {}
    
    for i in students:
        if i[1]>=threshold:
            accepted.append(i)
        else:
            refused.append(i)
    
    accepted.sort(key = lambda x:x[1],reverse = True)
    refused.sort(key = lambda x:x[1],reverse = False)
    
    res.__setitem__('Accepted',accepted)
    res.__setitem__('Refused',refused)
    
    return res