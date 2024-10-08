from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        print("Turning off...")
        break
    elif menu.find_drink(choice) != None:
        if coffee_maker.is_resource_sufficient(menu.find_drink(choice)) and money_machine.make_payment(menu.find_drink(choice).cost):
            coffee_maker.make_coffee(menu.find_drink(choice))
