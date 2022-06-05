############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def clear_console():
      os.system("cls" if os.name == 'nt' else "clear")

player_hand = []
dealer_hand = []

def hand_check(hand):
      hand_score = 0
      ace_count = 0
      
      for card in hand:
            hand_score += card

      for card in hand:
            if card == 11:
                  ace_count +=1
      
      while (hand_score > 21) and (ace_count != 0):
            hand_score -= 10
            ace_count -=1
      
      return hand_score

def blackjack_check(hand):
      return ((11 in hand) and (10 in hand))