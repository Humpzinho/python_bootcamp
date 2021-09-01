import pandas

alpha_file = pandas.read_csv(
    "Day 26 - NATO Alphabet\\nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for (index, row) in alpha_file.iterrows()}

result = []

word = input("Enter a word: ").upper()
new_list = [result.append(nato[letter]) for letter in word if letter in nato]

print(result)