import os
import random

import blackjack_modules

# globals
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_on = True


while game_on:
# Welcome to BlackJack
    print(blackjack_modules.logo)
    print("Welcome to Blackjack!\n")

    # Reset hands
    player_hand = []
    dealer_hand = []

    # Do you want to play a game of Blackjack?
    while True:
        start_game = input("Do you want to play a game of Blackjack? (Y/N)\n").lower()
        if start_game in ["y","n"]:
            break
        else:
            print("Invalid option. Please type Y/N\n")

    if start_game == "n":
        game_on = False
        print("Ok goodbye!")
        break

    # Deal initial hand to both player and computer
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))

    dealer_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    dealer_score = blackjack_modules.hand_check(dealer_hand)

    if blackjack_modules.blackjack_check(player_hand):
        print(f"\nBlackJack for you! In your hand is {player_hand}. You win!")
        break

    if blackjack_modules.blackjack_check(dealer_hand):
        print(f"\nBlackJack for Dealer!\nIn your hand is {player_hand}.\nIn dealer's hand is {dealer_hand}. You lose!")
        break
         
    # Show player his hand + current score
    player_score = blackjack_modules.hand_check(player_hand)
    print(f"\nIn your hand is {player_hand}. Your current score is {player_score}")

    # Show 1 of computer's card
    print(f"One of dealer's card is {dealer_hand[0]}.\n")

    # Ask if player wants to hit (Enter y to get another card). Loop until n.
    while True:
        while True:
            hit_choice = input("Would you like to draw another card. (Y/N)\n").lower()
            if hit_choice in ["y","n"]:
                break
            else:
                print("Invalid option. Please type Y/N\n")
        
        if hit_choice == "n":
            break

        else:
            # Show incremental hand + score
            player_hand.append(random.choice(cards))
            player_score = blackjack_modules.hand_check(player_hand)
            print(f"You were dealt {player_hand[-1]}")

            # Check if bust, instant lose
            if player_score > 21:
                break

            else:
                print(f"In your hand is {player_hand}. Your current score is {player_score}")


    if player_score > 21:
        print("You've bust. Game Over")

    elif dealer_score > player_score:
        print(f"In dealer's hand is {dealer_hand}. Dealer's score is {dealer_score}.")
        print("Dealer Wins. Game Over!")

    elif dealer_score == player_score:
        print(f"In dealer's hand is {dealer_hand}. Dealer's score is {dealer_score}.")
        print("Draw. Game Over!")
    
    elif dealer_score < player_score:
        # Computer hit phase. If below 16, Have to hit. Loop until above 16.
        print(''' 
=============================
Time for Dealer's Draw Phase!
=============================

''')
        while (dealer_score < player_score) and (dealer_score < 21):
            dealer_hand.append(random.choice(cards))
            dealer_score = blackjack_modules.hand_check(dealer_hand)
            print(f"Dealer drew {dealer_hand[-1]}\n")
            
            if dealer_score > 21:
                print(f"In dealer's hand is {dealer_hand}. Dealer's score is {dealer_score}.")
                print("Dealer's bust. You Win! Game Over.")
            
            elif dealer_score > player_score:
                print(f"In dealer's hand is {dealer_hand}. Dealer's score is {dealer_score}.")
                print("Dealer Wins. Game Over!")
                break

            elif dealer_score == player_score:
                print(f"In dealer's hand is {dealer_hand}. Dealer's score is {dealer_score}.")
                print("Draw. Game Over!")
                break

    while True:
        play_again = input("Would you like to play again. (Y/N)\n").lower()
        if play_again in ["y","n"]:
            break
        else:
            print("Invalid option. Please type Y/N\n")
    
    if play_again == "n":
        game_on = False
        print("Thank you for playing Blackjack. Goodbye!")
        break

    else:
        blackjack_modules.clear_console()

