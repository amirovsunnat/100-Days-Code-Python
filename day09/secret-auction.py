from logo import logo
import os

print(logo)
print("\nWelcome to our secret auction program !")
bidders = {}
continue_game = True
while continue_game:
    name = input("What is your name?:\n").title()
    bid = float(input("What is your bid?: \n$"))
    promt = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    bidders[name] = bid
    if promt.lower() == "no":
        continue_game = False
    else:
        os.system('cls')

highest_bid = 0
highest_bidder = "" 
for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
        highest_bidder = bidder
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")