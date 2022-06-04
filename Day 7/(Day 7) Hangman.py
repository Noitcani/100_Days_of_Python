# Imports and Functions
import random, os, string
import hangman_ascii, hangman_wordlist

# Art and wordlist
life_stage = hangman_ascii.live_stage
word_list = hangman_wordlist.word_list

# Clear console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Play again check
def play_again_check():
    play_again = ""
    play_again = input("Good Game! Do you want to play again? (Y/N)" +"\n")

	# Validity check
    valid_input = True
    if play_again not in ["Y","y","N","n"]:
        valid_input = False

	# Loop till valid
    while not valid_input:
        play_again = input("Invalid entry. "+ "Good Game! Do you want to play again? (Y/N)" + "\n")
        
        if play_again in ["Y","y","N","n"]:
            valid_input = True

    return play_again

# Choose alphabet
def getuser_choice():
    user_choice = ""
	 # Initial Try
    user_choice = input("What alphabet would you like to guess? (See available ones above)" +"\n").lower()

	# Validity check
    valid_input = True
    if user_choice not in avail_choices:
        valid_input = False

    # Loop till valid
    while not valid_input:
        user_choice = input("Invalid entry. "+ "What alphabet would you like to guess? (See available ones above)" + "\n").lower()
        if user_choice in avail_choices:
            valid_input = True

    return user_choice

# global vars
game_on = True
round_on = True

# Welcome

print(hangman_ascii.logo)
print("Welcome to Hangman!")

# Start Game
while game_on:

	# Pick a random word from list
	chosen_word = random.choice(word_list)

	# Generate guess progress
	guess_progress = "_"*len(chosen_word)

	# Generate avail_choices:
	avail_choices = list(string.ascii_lowercase)

	# Set no. of lives for game
	lives = 6



	# Start guessing loop, while not dead and word not guessed
	while round_on == True:
	# Display guess_progress
		print("\nWord to guess: " + guess_progress)

		# Display avail_choices list (A-Z).
		print("\nYou can choose to guess:")
		print(avail_choices)
		
		# Display no. of lives
		print(f"\nYou have {lives} lives left.")
		print(life_stage[lives])

		# Ask for user input for letter
			# Some check for letter not already chosen
		user_choice = getuser_choice()
		
		# Display letter chosen, pop letter chosen from avail
		print(f"You've chosen {user_choice}")
		avail_choices.remove(user_choice)

		# If loop for letter_exists or not
		if user_choice in chosen_word:
			
			# If exists, mark positions on blanks
			print(f"Nice! {user_choice} was in the word.")
			index_char = 0
			for char in chosen_word:
				index_char +=1
				if char == user_choice:
					guess_progress = guess_progress[:index_char-1] + user_choice + guess_progress[index_char:]

		# Elif doesn't exist, live - 1
		else:
			print(f"Sorry, {user_choice} was not in the word.")
			lives -=1


		# Check if word complete (no more blanks)
		if "_" not in guess_progress:
			clearConsole()
			print(f"Congrats! The word was {chosen_word}. You have guessed it in time!")
			round_on = False
			break

		# Check if dead (lives = 0). If dead, print game over
		elif lives == 0:
			clearConsole()
			print(life_stage[lives])
			print(f"You failed. The answer was {chosen_word}. Man hung. Game Over!")
			round_on = False
			break

		else:
			clearConsole()

	# If game over, ask Play Again?
	play_again = play_again_check()
	if play_again in ["N","n"]:
		game_on = False
		exit()
	
	else:
		game_on = True
		round_on = True
		clearConsole()