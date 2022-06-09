MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Globals
money = 0.0

coin_list = {
    "Quarters": 0.25,
    "Dimes": 0.10,
    "Nickles": 0.05,
    "Pennies": 0.01,
}


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def user_choice():
    while True:
        input_choice = input("What would you like? (Espresso/Latte/Cappuccino):   ").lower()
        if input_choice not in ["espresso", "latte", "cappuccino", "off", "report"]:
            print("Sorry that's invalid. Please enter a valid choice.")
        else:
            break
    return input_choice


# TODO: 4. Check resources sufficient?
def check_resource(check_choice):
    enough_resource = True
    for i in resources.keys():
        if resources[i] < MENU[check_choice]["ingredients"][i]:
            print(f"Sorry! There is not enough {i}")
            enough_resource = False
    return enough_resource


# TODO: 5. Process coins
def process_coins():
    coin_collected = {}
    amount_collected = 0.0

    for coin_type in coin_list.keys():
        while True:
            coin_collected[coin_type] = input(f"How many {coin_type} to insert:  ")
            try:
                int(coin_collected[coin_type])
            except ValueError:
                print("Sorry, invalid entry. Please key in an integer.")
            else:
                coin_collected[coin_type] = int(coin_collected[coin_type])
                break

    for coin_value, coin_count in zip(coin_list.keys(), coin_collected.keys()):
        amount_collected += coin_list[coin_value] * coin_collected[coin_count]

    print(f"You've inserted ${amount_collected:.2f} worth of coins.")
    return amount_collected


# TODO: 6. Check transaction successful?
def check_transaction(choice_var, amount):
    if MENU[choice_var]["cost"] > amount:
        print(f"Sorry that's not enough money. ${amount:.2f} refunded.")
        return False
    elif MENU[choice_var]["cost"] < amount:
        print(f"Your change is ${amount - MENU[choice_var]['cost']:.2f}")
        return MENU[choice_var]['cost']
    else:
        return MENU[choice_var]['cost']


# TODO: 7. Make_Coffee.
def make_coffee(choice_var, resource_pool):
    for i in resource_pool.keys():
        resource_pool[i] -= MENU[choice_var]["ingredients"][i]
    print(f"Here is your {choice_var}! Enjoy!")
    return resource_pool


# Welcome
print("Welcome to Coffee Machine\n")

while True:
    choice = user_choice()
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money:.2f}")

    elif choice == "off":
        print("Thank you for using coffee machine. Turning off now")
        break

    else:
        resource_sufficient = check_resource(choice)

        if resource_sufficient:
            amount_rec = process_coins()

            money_added = check_transaction(choice, amount_rec)
            if money_added:
                money += money_added
                make_coffee(choice, resources)
                