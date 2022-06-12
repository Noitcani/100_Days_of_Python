import random
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

app_run = True

while app_run:
    # Welcome to the Number Guessing Game!
    print("""
    ====================================
    Welcome to the Number Guessing Game!
    ====================================
    """)
    
    print("\n")
    print("I'm thinking of a number between 1 and 100")

    # Set target_number
    target_number = random.choice(list(range(1,101)))

    # Choose a difficulty
    while True:
        difficulty = input("Choose a difficulty, 'Easy' or 'Hard'.    ").lower()
        if difficulty not in ["easy","hard"]:
            print("Invalid. Please type either 'Easy' or 'Hard'.")
        else:
            break

    # Set lives
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5

    # Guessing loop, while target not hit and lives !=0

    target_hit = False
    while (target_hit == False) and (lives != 0): 
        # Print number of lives
        print(f"\nYou have {lives} attempt remaining to guess the number!   ")
        # Get user's guess
        while True:
            user_guess = input("\nMake a guess:   ")
            try: 
                int(user_guess)
            except ValueError:
                print("Invalid. Please guess an integer between 1 and 100")
                continue
            else:
                if int(user_guess) not in range(1,101):
                    print("Invalid. Please guess an integer between 1 and 100")
                else:
                    user_guess = int(user_guess)
                    break
        
        # Check and say direction towards target and Deduct live if fail
        if target_number == user_guess:
            print(f"\nWell done! The number was indeed {target_number}! You win!")
            break
        
        else:
            if target_number < user_guess:
                print("\n[[Too High!]] \nGuess Again.")
                lives -= 1
            else:
                print("\n[[Too Low!]] \nGuess Again.")
                lives -= 1

    if lives == 0:
        print(f"\nSorry, you ran out of lives! The number was {target_number} \n   Game Over!")

    while True:
        play_again = input("\n\nDo you want to play again? (Y/N)    ").lower()
        if play_again not in ["y","n"]:
            print("Invalid. Please type either 'Y' or 'N'.")
        else:
            break

    if play_again == "n":
        print("\nThanks for playing! Goodbye!")
        app_run = False
        break

    else:
        clear_console()