dictionary = open("words_alpha.txt", "r")
count = 0
for line in dictionary:
    # there appears to be a space and newline character at the end of each line
    line = line[0:len(line)-2]
    print(line)
    if count < 5:
        count = count + 1
    else:
        break

dictionary.close()
