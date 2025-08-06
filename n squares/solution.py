def draw_n_squares(n):
    upper_border = "+---"
    side_border = "|   "
    string=""
    for i in range(n):
        string += n*upper_border + "+\n"
        string += n*side_border + "|\n"
    
    string += n*upper_border + "+\n"
    return string