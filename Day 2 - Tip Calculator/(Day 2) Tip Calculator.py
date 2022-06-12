# Welcome
print("Welcome to the tip calculator!")

# Ask for total bill
total_bill = float(input("What was the total bill?\n$"))

#Ask for tip
tip_valid = False
while not tip_valid:
  tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
  if tip in [10,12,15]:
    tip_valid = True

# Ask for no. of people
pax = int(input("How many people to split the bill?\n"))

#Calculate share
share = "{:.2f}".format((total_bill*(1+(tip/100)))/pax,2)

#Output share
print(f"Each person should pay: ${share}")