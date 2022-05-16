# data from https://github.com/dwyl/english-words/
import numbers as num
one = num.Numbers(1, None, None, None, None)
two = num.Numbers(2, "a", "b", "c", None)
three = num.Numbers(3, "d", "e", "f", None)
four = num.Numbers(4, "g", "h", "i", None)
five = num.Numbers(5, "j", "k", "l", None)
six = num.Numbers(6, "m", "n", "o", None)
seven = num.Numbers(7, "p", "q", "r", "s")
eight = num.Numbers(8, "t", "u", "v", None)
nine = num.Numbers(9, "w", "x", "y", "z")
zero = num.Numbers(0, "+", None, None, None)
keypad = [one, two, three, four, five, six, seven, eight, nine, zero]
to_decode = input("please input numbers: ")
in_progress_string = ""
letter_list = []
word_list = []
letter_to_check = ''
original_letter_list = []
current_place = len(to_decode)-1
confirmed_words = []

def convert_to_letter(conversion_number, key):
    if conversion_number == 0:
        return key.letter0
    elif conversion_number == 1:
        return key.letter1
    elif conversion_number == 2:
        return key.letter2
    else:
        return key.letter3


def convert_to_key(number):
    for scan in keypad:
        if scan.number == int(number):
            current_number = scan
            return current_number


def check_letter_pos(letter):
    for a in keypad:
        for b in range(4):
            if letter == a.number_list[b]:
                return b


def letter_to_key(letter):
    for a in keypad:
        for b in range(4):
            if letter == a.number_list[b]:
                return a


def check_against_dictionary(words):
    word_length = words[0]
    if len(word_length) < 3:
        add = open("organized_wrods/1-2_long", "r")
    elif len(word_length) == 3:
        add = open("organized_wrods/3_long.txt", "r")
    elif len(word_length) == 4:
        add = open("organized_wrods/4_long.txt", "r")
    elif len(word_length) == 5:
        add = open("organized_wrods/5_long.txt", "r")
    elif len(word_length) == 6:
        add = open("organized_wrods/6_long.txt", "r")
    elif len(word_length) == 7:
        add = open("organized_wrods/7_long.txt", "r")
    elif len(word_length) == 8:
        add = open("organized_wrods/8_long.txt", "r")
    elif len(word_length) == 9:
        add = open("organized_wrods/9_long.txt", "r")
    elif len(word_length) == 10:
        add = open("organized_wrods/10_long.txt", "r")
    else:
        add = open("organized_wrods/11+_long.txt", "r")
    for lines in add:
        for wordies in words:
            if wordies == lines[0:len(lines)-1]:
                confirmed_words.append(wordies)
    add.close()
    print(words)


for w in to_decode:
    letter_list.append(convert_to_letter(0, convert_to_key(w)))
    original_letter_list.append(convert_to_letter(0, convert_to_key(w)))
while current_place > -1:
    current_place = len(to_decode)-1
    for x in range(4):
        letter_to_check = convert_to_letter(x, convert_to_key(to_decode[current_place]))
 # i think this is wrong but ill cross that bridge when i get there
        letter_list[current_place] = letter_to_check
        for y in letter_list:
            if y is not None:
                in_progress_string = in_progress_string + y
            else:
                in_progress_string = in_progress_string + "-"
        word_list.append(in_progress_string)
        print(in_progress_string)
        in_progress_string = ""
    current_place = current_place - 1
    while check_letter_pos(letter_list[current_place]) == 3 or letter_list[current_place] is None:
        letter_list[current_place] = original_letter_list[current_place]
        current_place = current_place - 1
    letter_list[current_place] = convert_to_letter(check_letter_pos(letter_list[current_place]) + 1,
                                                   letter_to_key(letter_list[current_place]))
print(word_list)
check_against_dictionary(word_list)
print(confirmed_words)
