from data import MENU, resources
total_cost = 0


def order():
    input_order = input("What would you like? (espresso/latte/cappuccino): ")
    if input_order in MENU:
        if check(input_order) == True:
            resources["water"] -= MENU[input_order]["ingredients"]["water"]
            resources["milk"] -= MENU[input_order]["ingredients"]["milk"]
            resources["coffee"] -= MENU[input_order]["ingredients"]["coffee"]
            print("Here is ${:.2f} in change.".format(change_money))
            print(f"Here is your {input_order}!")
            order()
        else:
            order()
    if input_order == "report":
        print(
            f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${total_cost}')
        order()
    elif input_order == "off":
        print("Turning off...")
        quit()
    else:
        print("That's not in menu.\nTry again.")
        order()


def check(input_order):
    if resources["water"] >= MENU[input_order]["ingredients"]["water"]:
        if resources["coffee"] >= MENU[input_order]["ingredients"]["coffee"]:
            global total_cost
            global change_money
            print("Please insert coins.")
            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickles = int(input("How many nickles?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01
            money = quarters + dimes + nickles + pennies
            change_money = money
            if money >= MENU[input_order]["cost"]:
                total_cost += MENU[input_order]["cost"]
                change_money = money - MENU[input_order]["cost"]
                money -= MENU[input_order]["cost"]
                return True
            else:
                print("Sorry, that's not enough money.\nMoney refunded.")
                return False
        else:
            print("Sorry, there is not enough coffee.")
            order()
    else:
        print("Sorry, there is not water.")
        order()


order()
