def battery_charge(num):
    ans=round(num/10)
    no_of_bars = ans * "❚"
    no_of_spaces = 10 - len(no_of_bars)  
    string = "[" + no_of_bars + no_of_spaces * " " + "]"
    
    print(string)
    print(num,"%")