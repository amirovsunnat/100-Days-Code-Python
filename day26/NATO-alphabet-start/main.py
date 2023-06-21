import pandas

phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet_dict = {row.letter: row.code for (index, row) in phonetic_alphabet.iterrows()}


def nato():
    user_word = input("Enter a word: ").upper()
    letter_word = [phonetic_alphabet_dict[letter] for letter in user_word]
    print(letter_word)


while True:
    try:
        nato()
        break
    except KeyError:
        print("Sorry only letters are allowed.")

