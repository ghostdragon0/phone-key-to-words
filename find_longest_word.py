dictionary = open("words_alpha.txt", "r")
longest_word = ""
amount_of_letters = 0
for line in dictionary:
    if len(line)-2 > amount_of_letters:
        amount_of_letters = len(line)-2
        longest_word = line[0:len(line)-2]

# the answer was dichlorodiphenyltrichloroethan
print(longest_word)
dictionary.close()
