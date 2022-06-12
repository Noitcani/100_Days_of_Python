# Encode/decode input
# Type 'encode' to encrypt, 'decode' to decrypt

def get_encode_decode():        
    encode_decode = ""

    # Initial Try
    encode_decode = input("Type 'encode' to encrypt, 'decode' to decrypt." +"\n").lower()

    # Validity check
    valid_input = True
    if encode_decode not in ["encode","decode"]:
        valid_input = False

    # Loop till valid
    while not valid_input:
        encode_decode = input("Invalid entry. "+ "Type 'encode' to encrypt, 'decode' to decrypt." + "\n").lower()
        if encode_decode in ["encode","decode"]:
            valid_input = True

    return encode_decode

def get_shift():
    shift = ""

    # Initial Try
    shift = input("Please key in the shift number" +"\n")

    # Validity check
    valid_input = True
    if not shift.isdigit():
        valid_input = False

    # Loop till valid
    while not valid_input:
        shift = input("Invalid entry. "+ "Please key in the shift number" + "\n")
        if shift.isdigit():
            valid_input = True

    return int(shift)

def get_go_again():

    go_again = ""

    # Initial Try
    go_again = input("Do you want to go again? (Y/N)" +"\n")

    # Validity check
    valid_input = True
    if go_again not in ["Y","y","N","n"]:
        valid_input = False

    # Loop till valid
    while not valid_input:
        go_again = input("Invalid entry. "+ "Do you want to go again? (Y/N)" + "\n")
        if go_again in ["Y","y","N","n"]:
            valid_input = True

    return go_again

# Clear console
def cls():
    import os
    os.system('cls' if os.name=='nt' else 'clear')