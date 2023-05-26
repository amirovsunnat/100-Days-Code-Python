import random as r
from logo import logo
from os import system

def deal_card():
    """Returns random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = r.choice(cards)
    return card

def calculate_score(cards):
    """Takes list of cards, and returns score calculated from the cards"""
    # checking if user or pc has blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # if 11 inside of cards and total is over 21, we replace it with 11 with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare_score(user_score, pc_score):
    if user_score == pc_score:
        return "Draw 🙃"
    elif pc_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif pc_score > 21:
        return "Opponent went over. You win 😃"
    elif user_score > pc_score:
        return "You win 🥳"
    elif pc_score > user_score:
        return "You lose. Opponent wins ☹️"

def play_game():  
    print(logo)
    user_cards = []
    pc_cards = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        pc_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        pc_score = calculate_score(pc_cards)
        print(f"Your cards {user_cards}, and total is {user_score}")
        print(f"Pc's one card is {pc_cards[0]}")

        if user_score == 0 or pc_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True    

    while pc_score != 0 and pc_score < 17:
        pc_cards.append(deal_card())
        pc_score = calculate_score(pc_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Pc's final hand: {pc_cards}, final score: {pc_score}")
    print(compare_score(user_score, pc_score))

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower() == "yes":
    system("cls")
    play_game()