import pandas as pd

data = pd.read_csv("day26/NATO-alphabet-start/nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        user_word = [nato_dict[let] for let in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(user_word)


generate_phonetic()
