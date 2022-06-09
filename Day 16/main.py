from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Welcome
print("Welcome to Coffee Machine\n")

coffee_machine = CoffeeMaker()
money_bank = MoneyMachine()
menu_list = Menu()
app_run = True

while app_run:
    user_choice = input("What would you like?" + menu_list.get_items() + ":   ").lower()
    if user_choice == "off":
        print("Thank you! Goodbye!")
        app_run = False
        break
    elif user_choice == "report":
        coffee_machine.report()
        money_bank.report()
    else:
        drink = menu_list.find_drink(user_choice)
        if drink:
            drink_available = coffee_machine.is_resource_sufficient(drink)
            if drink_available:
                payment = money_bank.make_payment(drink.cost)
                if payment:
                    coffee_machine.make_coffee(drink)
