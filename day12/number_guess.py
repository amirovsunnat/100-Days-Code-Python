from logo import logo
from random import randint


# computer chooses random number
random_number = randint(1, 100)
lives = 0 # to handle user progress
print(logo)
print("Welcome to the Number Guessing Game!")
game_is_not_over = True # to stop while loop if number is found
difficulty_level = input("Choose a difficulty level. Type 'easy' for easy level, or type 'hard' for hard level: ").lower()  # for giving lives

# we used if statement to check user preferences and give lives according to their choice
if (difficulty_level == "easy"):
    lives = 10
elif (difficulty_level == "hard"):
    lives = 5
else:
    print("Please make sure that you entered valid difficulty level!")

if (difficulty_level == "easy" or difficulty_level == "hard"):
    while game_is_not_over:
        print(f"You have {lives} attempts remaining to guess the number.")
        user_guess = int(input("Enter your guess: "))
        lives -= 1
        # check if user run out of lives
        if lives == 0:
            game_is_not_over = False
            print("You have run out of guess. You have lost! SORRY!!!!!")
            break
        elif (user_guess > random_number):
            print("Too high.")
            print("Guess again.")
        elif (user_guess < random_number):
            print("Too low")
            print("Guess again.")
        elif (user_guess == random_number):
            print(f"Congratulations! The number was {user_guess}")
            game_is_not_over = False
        



