letter_count = {}
f= open("words.txt")
letter_counter = 0

for line in f:
    for letter in line:
        letter_count[letter] = letter_count.get(letter,0)+1
        letter_counter += 1

for key,value in letter_count.items():
    print(f"{key}: {value/letter_counter:0.2f}")