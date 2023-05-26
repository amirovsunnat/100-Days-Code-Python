# Day 3. Building Treasure Island Game

# Algorithm for this game:
# 1. Draw chest
# 2. Welcoming to user
# 3. Explaining the game
# 4. Giving question, checking the answer with if and else and storing the answer to variables.
# 5. Regarding which answer is chosen maintaining the game.
# It runs until the answers end or user conditionally lose, or wise versa win.



print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')


print("""Welcome to Treasure Island\nYour mission is to find the treasure""")
crossRoad = input(f"You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if (crossRoad.lower() == "left"):
    lake = input(f"You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for boat. Type 'swim' to swim across\n")
    if (lake.lower() == "swim"):
        print("You get attacked by an angry trout. Game Over.")
    else:
        islandUnharmed = input(f"""You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n""")
        if(islandUnharmed.lower() == "red"):
            print(f"It's a room full of fire. Game Over")
        elif (islandUnharmed.lower() == "yellow"):
            print(f"You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
else:
    print(f"You fell into a hole. Game Over.")

 