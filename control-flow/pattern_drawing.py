# Objective: Utilize while loops and nested for loops to draw a simple text-based pattern.

# Instructions:
# 1. Prompt User for Pattern Size.
# 2. Draw the Pattern using a while loop for rows and a for loop for columns.

# Prompt the user to enter a positive integer for the size of the pattern.
# Convert the input to an integer.
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the outer while loop (for rows).
# This counter will keep track of how many rows have been printed.
row_count = 0

# Use a while loop to iterate through each row of the pattern.
# The loop continues as long as the row_count is less than the desired 'size'.
while row_count < size:
    # Inside the while loop, use a for loop to print asterisks for the current row.
    # This loop iterates 'size' number of times, printing one asterisk for each column.
    for col_count in range(size):
        # Print an asterisk.
        # The 'end=""' argument ensures that the print function does NOT add a newline
        # after each asterisk, so they stay on the same line.
        print("*", end="")
    
    # After the inner for loop completes (meaning a full row of asterisks has been printed),
    # print a newline character to move to the next line/row for the next iteration of the while loop.
    print() 
    
    # Increment the row counter to move to the next row.
    row_count += 1

