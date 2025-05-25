# Prompt the user to input their current age
# The input() function reads a line from input, and int() converts it to an integer
current_age = int(input("How old are you? "))

# Assume the current year is 2023 and we want to calculate age in 2050.
# The difference in years is 2050 - 2023 = 27 years.
years_to_add = 27

# Calculate the user's age in 2050
future_age = current_age + years_to_add

# Print the user's age in 2050 in the specified format
print(f"In 2050, you will be {future_age} years old.")
