# HANGMAN
from hangman_art import stages, logo
from hangman_words import word_list
import random as r

chosen_word = r.choice(word_list)
chosen_word_list = []
for a in range(len(chosen_word)):
    chosen_word_list.append("_")


game_end = False
lives = 6

print(f"{logo}\n")
print(chosen_word)
while not game_end:
    user_guess = input("Type your guess here:\n").lower()

    # check user guess is inside of chosen_word_list
    if user_guess in chosen_word_list:
      print(f"You have already guessed {user_guess}")

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == user_guess:
            chosen_word_list[i] = letter

    if user_guess not in chosen_word:
        lives -= 1
        print(f"You have guessed wrong letter, and you lose one life.")
        if lives == 0:
            game_end = True
            print("You lose.....")

    print(" ".join(chosen_word_list))

    if "_" not in chosen_word_list:
        game_end = True
        print("You WIN !!!!!")
    
    print(stages[lives])




    