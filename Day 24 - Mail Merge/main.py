#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
    for item in name_list:
        name_list[name_list.index(item)] = item.replace("\n", "")

print(name_list)

with open("./Input/Letters/starting_letter.txt", mode='r') as f:
    letter_template = f.read()

for name in name_list:
    filename = f"letter_for_{name}.txt"
    named_letter = letter_template.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{filename}", mode="w") as x:
        x.write(named_letter)

