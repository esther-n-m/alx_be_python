# Prompt the user to enter the first number.
# Convert the input string to a float to allow for decimal numbers.
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number.
# Convert the input string to a float.
num2 = float(input("Enter the second number: "))

# Prompt the user to choose an operation.
operation = input("Choose the operation (+, -, *, /): ")

# Use a match-case statement to perform the selected operation.
# This is available in Python 3.10+ and provides a cleaner way
# to handle multiple conditional branches compared to if-elif-else for simple equality checks.
match operation:
    # Case for addition
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    # Case for subtraction
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    # Case for multiplication
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    # Case for division
    case '/':
        # Check for division by zero before performing the operation
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            # Handle the division by zero error gracefully
            print("Cannot divide by zero.")
    # Default case for any unsupported operation input
    case _:
        print("Invalid operation. Please choose from +, -, *, /.")

