class MenuItem:
    """Menu Item class used models to each menu"""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the menu with the drink"""
    def __init__(self):
        self.menu = [
            MenuItem(name="expresso", cost=1.5, water=50, milk=0, coffee=18),
            MenuItem(name="latte", cost=2.5, water=200, milk=150, coffee=24),
            MenuItem(name="cappuccino", cost=3, water=250, milk=50, coffee=24)
        ]

    def get_items(self):
        """Returns all the names of the available menu items as a concatenated string."""
        coffee_names = ""
        for i in self.menu:
            coffee_names += f"{i.name}/"
        return coffee_names

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,
        otherwise returns None."""
        for a in self.menu:
            if a.name == order_name:
                return a

        print(f"Sorry, {order_name} is not available!")

