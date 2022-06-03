print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


#Write your code below this line 👇

# Choice 1: Crossroad L/R?
crossroad_valid = False
while not crossroad_valid:
  crossroad = input("You've reached a crossroad. Do you want to go 'Left' or 'Right'?\n").lower()
  if crossroad in ["left","right"]:
    crossroad_valid = True

if crossroad != "left":
  print("You fell into a hole and died. Game over")

else:
  # Choice 2: Swim or wait
  swim_valid = False
  while not swim_valid:
    swim = input('''
You've reached a river.
You can either swim or wait for a boat.
Do you want to 'Swim' or 'Wait'?

''').lower()
    if swim in ["swim","wait"]:
      swim_valid = True

  if swim != "wait":
    print("You were eaten by a hippo. Game over.")
  
  else:
    # Choice 3: Which Door?
    door_valid = False
    while not door_valid:
      door = input('''

You've arrived in front of 3 doors.
Red, Blue or Yellow.
Which do you open?
                   
''').lower()
      if door in ["red","blue","yellow"]:
        door_valid = True

    if door == "red":
      print("You open a door to fiery hell and burn to death. Game over.")

    elif door == "blue":
      print("You open a door to huge beasts and were immediately eaten. Game over")

    else:
      print("\nYou open the door and there it is, the treasure.\n\nYou win!")
