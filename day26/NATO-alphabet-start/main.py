import pprint

import pandas as pd

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("day26/NATO-alphabet-start/nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = [nato_dict[let] for let in input("Enter a word: ").upper()]
print(user_word)
