def how_to_pay(amount,currency):
    ans = {}
    currency.sort()
    
    
    index=len(currency)-1
    while True:
        note = amount//currency[index]
        remaining = amount%currency[index]
        ans.__setitem__(currency[index],note)
        amount = remaining
        index-=1
        if remaining==0:
            return ans
    