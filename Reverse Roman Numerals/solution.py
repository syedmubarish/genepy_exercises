def from_roman_numeral(roman_numeral):
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    
    roman_numeral_list = list(roman_numeral)
    
    i=0
    
    while i < len(roman_numeral_list):
        if i==len(roman_numeral_list)-1:
            total += roman_map[roman_numeral_list[i]]
        elif roman_map[roman_numeral_list[i]]<roman_map[roman_numeral_list[i+1]]:
            total -= roman_map[roman_numeral_list[i]]
        else:
            total += roman_map[roman_numeral_list[i]]
        i=i+1
    return total