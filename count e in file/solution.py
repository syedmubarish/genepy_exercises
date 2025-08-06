count = 0
with open("words.txt") as f:
    for line in f:
        for letter in line:
            if letter =='e':
                count+=1


print(count)