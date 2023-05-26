from art import logo, vs
from game_data import data
from random import choice
from os import system


# printing account info in a nice way
def represent_data(account):
    """Takes account data, and returns information about the user"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, {description}, from {country}"


# compare user's guess
def compare(guess, a_account_fol, b_account_fol):
    """Takes user guess, then compares two accounts, and returns true or false"""
    if a_account_fol > b_account_fol:
        return guess == "A"
    else:
        return guess == "B"

print(logo)
account_b = choice(data)
game_is_not_finished = True
score = 0


while game_is_not_finished:
    # generate random user
    account_a = account_b   # every time we run the loop account a will be replaced if user guess is correct
    account_b = choice(data)
    if account_a == account_b:
        account_b = choice(data)

    # print accounts' info
    print(f"Account A: {represent_data(account_a)}")
    print(vs)
    print(f"Against B: {represent_data(account_b)}")

    # take user input
    user_guess = input("Which person you think has more followers? Type 'A' or 'B': ").upper()
    account_a_followers = account_a['follower_count']
    account_b_followers = account_b['follower_count']
    is_user_guess_correct = compare(user_guess, account_a_followers, account_b_followers)

    system("cls")
    print(logo)
    if is_user_guess_correct:
        score += 1
        print(f"You guessed right. Current score: {score}")
    else:
        game_is_not_finished = False
        print(f"Your guess was wrong. You lost. Final score: {score}")


