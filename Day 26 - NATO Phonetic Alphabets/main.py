import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Key in word for translation:   ").upper()

nato_list = [nato_dict[char] for char in word]

print(nato_list)

