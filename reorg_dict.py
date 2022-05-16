dictionary = open("words_alpha.txt", "r")
for line in dictionary:
    new_line = line[0:len(line)-2]
    if len(new_line) < 3:
        add = open("organized_wrods/1-2_long", "a")
    elif len(new_line) == 3:
        add = open("organized_wrods/3_long.txt", "a")
    elif len(new_line) == 4:
        add = open("organized_wrods/4_long.txt", "a")
    elif len(new_line) == 5:
        add = open("organized_wrods/5_long.txt", "a")
    elif len(new_line) == 6:
        add = open("organized_wrods/6_long.txt", "a")
    elif len(new_line) == 7:
        add = open("organized_wrods/7_long.txt", "a")
    elif len(new_line) == 8:
        add = open("organized_wrods/8_long.txt", "a")
    elif len(new_line) == 9:
        add = open("organized_wrods/9_long.txt", "a")
    elif len(new_line) == 10:
        add = open("organized_wrods/10_long.txt", "a")
    else:
        add = open("organized_wrods/11+_long.txt", "a")
    add.write(new_line + "\n")
    add.close()

