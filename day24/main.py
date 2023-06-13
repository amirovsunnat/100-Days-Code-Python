with open("./Input/Letters/starting_letter.txt", mode='r') as file:
    letter = file.readlines()

with open("./Input/Names/invited_names.txt", mode='r') as file:
    names = file.readlines()

for name in names:
    first_line = letter[0].replace("[name]", name.strip()).strip()
    with open(f"./Output/ReadyToSend/letter_for_{name.strip()}", mode='w') as file:
        file.write(f'{first_line}\n{"".join(letter[1:])}')









