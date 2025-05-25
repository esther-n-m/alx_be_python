# Prompt the user for their monthly income and convert it to a float
# Using float allows for decimal values in income
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses and convert it to a float
# Using float allows for decimal values in expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Define the simple annual interest rate as a decimal
annual_interest_rate = 0.05

# Calculate the projected savings after one year, incorporating the interest.
# Formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Display the user's monthly savings
# Using f-string for formatted output, rounding to 2 decimal places for currency
print(f"Your monthly savings are ${monthly_savings:.2f}.")

# Display the projected annual savings after including interest
# Using f-string for formatted output, rounding to 2 decimal places for currency
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
