def love_meet(bob, alice):
    bobset=set(bob)
    aliceset = set(alice)
    return bobset.intersection(aliceset)


def affair_meet(bob, alice, silvester):
    bobset=set(bob)
    aliceset = set(alice)
    silvesterset = set(silvester)
    
    affairset = aliceset.intersection(silvesterset)
    return affairset.difference(bobset)