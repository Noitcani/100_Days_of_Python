# Imports
import string, Caesar_Modules

# Globals
alphabets = list(string.ascii_lowercase + string.digits + string.ascii_uppercase + " ")
alphabets_dict = {i:alphabets[i] for i in range(len(alphabets))}
app_run = True

# Functions
## encrypt+decrypt func()
def caesar(pre_message,shift,mode):
    post_message = ""
    for char in pre_message:
        if char in alphabets:
            pre_index = alphabets.index(char) 
            
            if mode == "encode":
                post_index = (pre_index + shift) % len(alphabets)
            else:
                post_index = (pre_index - shift) % len(alphabets)
            
            post_message += alphabets[post_index]
        
        else:
            post_message += char
    
    print(f"Here is your {mode}d message! \n{post_message}")
        

# Welcome // Start App

while app_run:
    print("Welcome to Caesars Cipher Service!")

    # Encode/Decode?
    mode_choice = Caesar_Modules.get_encode_decode()
    message = input(f"Please enter the message you would like {mode_choice}d: \n")
    shift = Caesar_Modules.get_shift()

    caesar(message,shift,mode_choice)
        
    # Go_again?
    go_again = Caesar_Modules.get_go_again()
    if go_again in ["N","n"]:
        app_run = False
        quit()