# Prompt the user to enter a number.
# Convert the input string to an integer, as multiplication tables typically use whole numbers.
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate through numbers from 1 to 10 (inclusive).
# The range(1, 11) function generates numbers from 1 up to (but not including) 11.
for i in range(1, 11):
    # Calculate the product of the user's number and the current iterator 'i'.
    product = number * i
    
    # Print each line of the multiplication table in the specified format: "X * Y = Z".
    # f-strings are used for easy formatting and embedding variables.
    print(f"{number} * {i} = {product}")