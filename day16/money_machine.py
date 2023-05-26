class MoneyMachine:
    """Class for making payment"""
    def __init__(self):
        self.money_received = 0
        self.profit = 0

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns True when payment is accepted, or False if insufficient."""
        print("Please insert the coins")
        for item in self.COIN_VALUES:
            self.money_received += int(input(f"How many {item}: ")) * self.COIN_VALUES[item]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received-cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print(f"Sorry, that's not enough money. Money refunded.")
            return False




