#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_password = []
"""for i in range(nr_letters):
    random_letter = random.randint(0, i)
    random_letter = letters[random_letter]
    random_password.append(random_letter)
for j in range(nr_symbols):
    random_symbol = random.randint(0, j)
    random_symbol = symbols[random_symbol]
    random_password.append(random_symbol)
for k in range(nr_numbers):
    random_number = random.randint(0, k)
    random_number = numbers[random_number]
    random_password.append(random_number)

random.shuffle(random_password)
random_pass = "".join(random_password)
print(random_pass)
"""

for i in range(nr_letters):
    random_password.append(random.choice(letters))

for i in range(nr_symbols):
    random_password.append(random.choice(symbols))

for i in range(nr_numbers):
    random_password.append(random.choice(numbers))


random.shuffle(random_password)
random_pass = "".join(random_password)
print(f"Your password is: {random_pass}")



