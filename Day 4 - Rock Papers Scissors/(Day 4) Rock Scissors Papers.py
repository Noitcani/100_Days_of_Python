import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Welcome
print("Welcome to Rock Papers Scissors (against AI)")

def play_game():
  # Ask for player input
  player_choice_check = False

  while not player_choice_check:

    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if player_choice in [0,1,2]:
      player_choice_check = True

  # Generate AI choice
  ai_choice = random.randint(0,2)

  # Match choices to signs
  signs = {0:rock,1:paper,2:scissors}
  signs_str = {0:"Rock",1:"Paper",2:"Scissors"}
  player_sign = signs[player_choice]
  ai_sign = signs[ai_choice]


  # Display choices
  print("\n")
  print(f"You chose {signs_str[player_choice]}\n {player_sign}")
  print(f"AI chose {signs_str[ai_choice]}\n {ai_sign}")

  #Outcome logic
  ## Draws
  if player_choice == ai_choice:
    print("Draw. Nobody wins")

  ## Player Wins
  elif (player_choice,ai_choice) in [(0,2),(1,0),(2,1)]:
    print("You Win!")

  ## AI Wins
  else:
    print("AI Wins")

play_loop = True

while play_loop:
  play_game()

# Play again?
  play_again = input("Play again? (Y/N)\n")
  if play_again in ["N","n"]:
    play_loop = False
