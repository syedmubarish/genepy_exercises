def check_adam_number(num):
    rev_num = int(str(num)[::-1])
    
    square_num = num**2
    square_rev_num = rev_num**2
    
    if int(str(square_rev_num)[::-1]) == square_num:
        return True
    else:
        return False