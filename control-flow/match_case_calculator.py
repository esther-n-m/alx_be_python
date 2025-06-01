# simple_calculator.py

# 1. Get User Input
# First, the program prompts the user for the first number,
# then converts it to a floating-point number to handle decimals.
num1 = float(input("Enter the first number: "))

# Then, it prompts for the second number and converts it similarly.
num2 = float(input("Enter the second number: "))

# Next, the program asks the user to choose an operation symbol.
operation = input("Choose the operation (+, -, *, /): ")

# 2. Perform Calculation Using Conditional Logic
# The program then evaluates the chosen operation using an if-elif-else structure.
if operation == '+':
    # If the operation is addition, it calculates the sum.
    result = num1 + num2
    # Then, it prints the result.
    print(f"The result is {result}.")
elif operation == '-':
    # If the operation is subtraction, it calculates the difference.
    result = num1 - num2
    # Then, it prints the result.
    print(f"The result is {result}.")
elif operation == '*':
    # If the operation is multiplication, it calculates the product.
    result = num1 * num2
    # Then, it prints the result.
    print(f"The result is {result}.")
elif operation == '/':
    # If the operation is division, it first checks for division by zero.
    if num2 != 0:
        # If the second number is not zero, it performs the division.
        result = num1 / num2
        # Then, it prints the result.
        print(f"The result is {result}.")
    else:
        # If the second number is zero, it then prints an error message.
        print("Cannot divide by zero.")
else:
    # If none of the recognized operations are chosen, it then prints an error for invalid input.
    print("Invalid operation. Please choose from +, -, *, /.")