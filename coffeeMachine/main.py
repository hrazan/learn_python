MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money": 0.0,
}


def check_resource(menu_):
    if resources.get("water") >= MENU.get(menu_).get("ingredients").get("water") and resources.get("milk") >= MENU.get(menu_).get("ingredients").get("milk") and resources.get("coffee") >= MENU.get(menu_).get("ingredients").get("coffee"):
        return True
    else:
        return False


def check_money(menu_):
    quarters = float(input("input your quarters: "))
    dimes = float(input("input your dimes: "))
    nickles = float(input("input your nickles: "))
    pennies = float(input("input your pennies: "))
    total_money = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
    if total_money >= MENU.get(menu_).get("cost"):
        print(round(total_money, 10))
        print(MENU.get(menu_).get("cost"))
        print(f"total change {round(total_money-MENU.get(menu_).get("cost"), 2)}")
        return True
    else:
        print("not enough money")
        return False


while True:
    menu = input("espresso/latte/cappuccino/report? ").lower()

    if menu != "espresso" and menu != "latte" and menu != "cappuccino" and menu != "report":
        print("please pick between espresso/latte/cappuccino/report")
    elif menu == "report":
        print(f"water: {resources["water"]}")
        print(f"milk: {resources["milk"]}")
        print(f"coffee: {resources["coffee"]}")
        print(f"money: ${resources["money"]}")
    else:
        enough_resource = check_resource(menu)
        if enough_resource:
            enough_money = check_money(menu)
            if enough_money:
                resources["water"] -= MENU.get(menu).get("ingredients").get("water")
                resources["milk"] -= MENU.get(menu).get("ingredients").get("milk")
                resources["coffee"] -= MENU.get(menu).get("ingredients").get("coffee")
                resources["money"] += MENU[menu]["cost"]
        else:
            print("not enough resource")
