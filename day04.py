rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random as r

print("Welcome to our rock, paper, and scissors game!!!!!")
want_play = input("Do you want to play?(yes/no)\n")

# user choice
if (want_play.lower() == "yes"):
    choice = input("What do you choose? Type rock, paper, scissors\n")
    if (choice.lower() == "rock"):
        choice = rock
        print(choice)
    elif (choice.lower() == "paper"):
        choice = paper
        print(choice)
    elif (choice.lower() == "scissors"):
        choice = scissors
        print(choice)
    else:
        print("Please enter valid choice")

# computer choice
pc_num = r.randint(0, 2)
pc_choice = ''
print("Computer chose:")
if (pc_num == 0):
    pc_choice = rock
    print(pc_choice)
elif (pc_num == 1):
    pc_choice = paper
    print(pc_choice)
else:
    pc_choice = scissors
    print(pc_choice)

if (choice == rock) and pc_choice == rock:
    print("Equal")
elif(choice == rock) and pc_choice == paper:
    print("Computer win")
elif (choice == rock) and pc_choice == scissors:
    print("You win")
elif (choice == paper) and (pc_choice == rock):
    print("You win")
elif(choice == paper) and (pc_choice == scissors):
    print("Computer win")
elif (choice == paper) and pc_choice == paper:
    print("Equal")
elif (choice == scissors) and (pc_choice == scissors):
    print("Equal")
elif (choice == scissors) and (pc_choice == paper):
    print("You win")
else:
    print("Computer win")
    