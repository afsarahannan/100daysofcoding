# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

only_letters = False

while not only_letters:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        only_letters = True
    except KeyError:
        print("Sorry, please use letters in the english alphabet only.")
    else:
        print(output_list)

#or another way to solve this is

def generate_NATO():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, please use letters in the english alphabet only.")
        generate_NATO()
    else:
        print(output_list)

generate_NATO()
