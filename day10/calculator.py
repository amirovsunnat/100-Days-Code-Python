from logo import logo

# add
def add(number1, number2):
    """Takes two numbers, and returns total"""
    return number1 + number2

# subtract


def subtract(number1, number2):
    """Takes two numbers, subtract number2 from number1, and returns the result"""
    return number1 - number2

# multiply


def multiply(number1, number2):
    """Takes two numbers, multiply them, and returns the result"""
    return number1 * number2

# divide


def divide(number1, number2):
    """Takes two numbers, divide first number to second, and returns the result"""
    if number2 == 0:
        return "Number can't be divided by zero!!!!!"
    else:
        return number1 / number2


# dictionary for operators and functions
operators= {
    "+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    print(logo)
    number1 = float(input("Enter the first number: "))
    for operator in operators:
        print(operator)
    continue_calculation = True
    while continue_calculation:
        user_operator = input("Pick an operation: ")
        number2 = float(input("Enter the next number: "))
        current_operator = operators[user_operator]
        answer = current_operator(number1, number2)
        print(f"{number1} {user_operator} {number2} = {answer}")

        calculate_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculator, or type 'e' to exit.: ").lower()
        if calculate_again == "y":
            number1 = answer
        elif calculate_again == "n":
            calculate_again = False
            calculator()
        else:
            print("Enter valid option!")


calculator()