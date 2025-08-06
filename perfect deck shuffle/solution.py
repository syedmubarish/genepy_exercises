def perfect_shuffle(deck):
    firstHalf = deck[0:len(deck)//2]
    secHalf = deck[len(deck)//2:len(deck)]
    
    res = []
    
    for i in range(len(firstHalf)):
        res.append(firstHalf[i])
        res.append(secHalf[i])
    
    return res