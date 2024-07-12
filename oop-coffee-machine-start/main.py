from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

machineOn = True
# print(coffeMaker.report())
# print(menu.menu[0].name)
while machineOn:
    choice = input("What would you like?" + menu.get_items()).lower()
    if choice == "off":
        print()
    elif choice == "report":
        print()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        if coffeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            print("Thank you")
    else:
        print("input error")

