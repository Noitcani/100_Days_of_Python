#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get specs from user
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

generated_pw = []

# Get letters
for i in range(0,nr_letters):
    letter_to_add = random.choice(letters)
    generated_pw.append(letter_to_add)

# Get symbols
for i in range(0,nr_symbols):
    symbol_to_add = random.choice(symbols)
    generated_pw.append(symbol_to_add)

# Get numbers
for i in range(0,nr_numbers):
    number_to_add = random.choice(numbers)
    generated_pw.append(number_to_add)

# Shuffle and make into str
random.shuffle(generated_pw)
pw_final = ""
for x in generated_pw:
    pw_final += x

# Display generated pw
print(f"Your generated password is {pw_final}")