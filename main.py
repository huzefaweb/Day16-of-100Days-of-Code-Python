from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()  # Object created from coffee maker class
money_machine = MoneyMachine()  # Object created from MoneyMachine class
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items() # call the method using object menu
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()  # prints report 
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
