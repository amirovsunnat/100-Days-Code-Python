from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_coffee_serve_continue = True

while is_coffee_serve_continue:
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}): ").lower()
    if user_choice == "off":
        is_coffee_serve_continue = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)





