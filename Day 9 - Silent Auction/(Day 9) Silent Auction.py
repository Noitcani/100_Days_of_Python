import os
from turtle import clear

import art

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

# Globals
name_bid = {}
app_run = True

while app_run:
    # Welcome
    print(art.logo)
    print("\nWelcome to Silent Auction\n")

    # while more_users:
    while True:

        # Ask for name
        name = input("What is your name?\n")
 
        # Ask for bid
        while True:
            bid = input("What is your bid?\n$")
            try:
                float(bid)
            except:
                print("Sorry, I didn't understand that. Please key in a valid bid")
            else:
                bid = round(float(bid),2)
                print(f"Received your ({name}'s) bid of ${bid}")
                break
        
        # Store info
        name_bid[name] = bid

        # Ask if more bidders
        more_users = input("Is there another bidder? (Y/N)\n").lower()
        while True:
            if more_users in ["y","n"]:
                break

        if more_users == "n":
            clearConsole()
            break

        else:
            clearConsole()

    # Compute Winner
    winning_bid = 0
    winner_index = 0
    winners = []

    for bid in name_bid.values():
        if winning_bid < bid:
            winning_bid = bid

    for bid in name_bid.values():
        
        if bid == winning_bid:
            winners.append(list(name_bid.keys())[winner_index])

        winner_index += 1

    if len(winners) == 1:
        print(f"The winner is {winners[0]}, with a bid of ${name_bid[winners[0]]}!")

    else:
        print(f"The winners are {' '.join(winners)}, with equal bids of ${name_bid[winners[0]]}!")

    # Run app again?
    while True:
        run_again = input("Start another bid? (Y/N)\n").lower()
        if run_again not in ["y","n"]:
            print("Sorry, I didn't understand that. Please key Y/N")
        else:
            break
    
    if run_again == "n":
        print("Thank you for using this service. Goodbye.")
        app_run = False
    else:
        clearConsole()