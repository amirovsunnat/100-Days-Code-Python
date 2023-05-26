class CoffeeMaker:
    """Make coffee"""
    def __init__(self):
        self.resources = {
            "water": 10000,
            "milk": 6500,
            "coffee": 1800,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, coffee_name):
        """Returns True when the drink order can be made, False if ingredients are insufficient."""
        for item in coffee_name.ingredients:
            if self.resources[item] < coffee_name.ingredients[item]:
                print(f"Sorry, there is not enough {item}")
                return False
            else:
                return True

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")





