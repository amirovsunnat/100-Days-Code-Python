from data import MENU, resources, profit
from art import art

print(art)


# TODO: 3. Print report.
def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return f"Water: {water} ml\nMilk: {milk} ml\nCoffee: {coffee} g\nMoney: ${profit}"


# TODO: 4. Check resources sufficient?
def is_resource_sufficient(coffee_type):
    """Takes coffee type, and check if resources is enough to make, it returns True, otherwise False."""
    for item in coffee_type:
        if resources[item] >= coffee_type[item]:
            return True
        else:
            print(f"There is no enough {item}")
            return False


# TODO: 5. Process coins.
def process_coins():
    """Takes a user money, and returns total money."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total


# TODO: 6. Check transaction successful?
def check_transaction(coffee_cost, user_money):
    """Returns True and change if user has entered enough money, otherwise False"""
    if user_money < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(user_money - coffee_cost, 2)   # round the change at 2 decimal points
        print(f"Here is ${change} in change.")
        global profit
        profit += coffee_cost
        return True


# TODO: 7. Make Coffee.
def make_coffee(type_coffee, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {type_coffee} ☕️. Enjoy!")


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
continue_serving_coffee = True
while continue_serving_coffee:
    coffee_preference = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if coffee_preference == "off":
        continue_serving_coffee = False
    elif coffee_preference == "report":
        print(report())
    else:
        coffee_choice = MENU[coffee_preference]
        if is_resource_sufficient(coffee_choice['ingredients']):
            payment = process_coins()
            if check_transaction(coffee_choice['cost'], payment):
                make_coffee(coffee_preference, coffee_choice['ingredients'])






