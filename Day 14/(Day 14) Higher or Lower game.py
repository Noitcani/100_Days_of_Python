from random import shuffle
import os

from art import logo, vs
from gamedata import data


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def assign_account(dataset):
    shuffle(dataset)
    return dataset.pop()

# functions
def check_guess(guess,non_guess):
    if guess['follower_count'] > non_guess['follower_count']:
        return True
    else:
        return False


def higher_or_lower():
    # globals
    score = 0
    round_on = True
    round_data = data


    # Welcome
    print("\n" + logo +"\n")

    # Set up first a and b
    a_details = assign_account(round_data)
    b_details = assign_account(round_data)

    while round_on:

        # Print comparison pairs
        print(f"\nCompare A: {a_details['name']}, a {a_details['description']}, from {a_details['country']}\n")
        print(vs + "\n")
        print(f"Against B: {b_details['name']}, a {b_details['description']}, from {b_details['country']}\n")


        # Get user_guess
        while True:
            user_guess = input("Who has more followers? Type 'A' or 'B':    ").lower()
            if user_guess not in ["a","b"]:
                print("Invalid. Please type 'A' or 'B'")
            else:
                break

        if user_guess == "a":
            correct_guess = check_guess(a_details,b_details)
        else:
            correct_guess = check_guess(b_details,a_details)

        if correct_guess:
            score +=1
            clear_console()
            print("\n" + logo +"\n")
            print(f"You're right. Current score: {score}\n")
            a_details = b_details
            b_details = assign_account(round_data)
        else:
            clear_console()
            print(f"\nWrong guess, you lose! Your final score was: {score}\n")
            round_on = False

# Execute
app_run = True

while app_run:
    higher_or_lower()
    while True:
        play_again = input("Do you want to play again? (Y/N):    ").lower()
        if play_again == "y":
            break
        elif play_again == "n":
            print("Thank you for playing! Goodbye!")
            app_run = False
            break
        else:
            print("Invalid. Please type 'Y' or 'N'")