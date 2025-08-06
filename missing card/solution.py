def missing_card(cards):
    color = {"S", "H", "D", "C"}
    value = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
    
    for c in color:
        for v in value:
            if c+v not in cards:
                return c+v
        