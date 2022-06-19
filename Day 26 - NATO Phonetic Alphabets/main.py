import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

while True:
    word = input("Key in word for translation:   ").upper()
    try:
        nato_list = [nato_dict[char] for char in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    
    else:
        break

print(nato_list)

