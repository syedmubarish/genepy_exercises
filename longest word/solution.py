def longest_word(text):
    word_list = text.split()
    print(word_list)
    longestWord = word_list[0]
    for word in word_list:
        if len(word)>len(longestWord):
            longestWord = word
    
    return longestWord