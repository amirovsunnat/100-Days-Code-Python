from logo import logo
from alphabet import alphabet


def encrypt_decrypt(message, shifting_number, direction_method):
    new_message = ''
    wrong_type = True
    for letter in message:
        if letter in alphabet:
            index_of_letter = alphabet.index(letter)
            if direction == "encode" or direction_method == "decode":
                if direction_method == "encode":
                    new_index = index_of_letter + shifting_number
                elif direction_method == "decode":
                    new_index = index_of_letter - shifting_number
                new_letter = alphabet[new_index]
                new_message += new_letter
            else:
                wrong_type = False
        else:
            new_message += letter
    if wrong_type:
        if direction_method == "encode":
            print(f"Your encrypted message is : {new_message}")
        else:
            print(f"Your decrypted message is : {new_message}")
    else:
        print("Please choose a valid type of encrypting!")


print(logo)
is_continue = True
while is_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    encrypt_decrypt(message=text, shifting_number=shift, direction_method=direction)

    prompt = input("Do you want to encrypt again? Type (yes) or (no)\n")
    if prompt.lower() == "no":
        is_continue = False