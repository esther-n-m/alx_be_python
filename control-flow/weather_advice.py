# Prompt the user for the current weather condition.
# The input is converted to lowercase to make the comparison case-insensitive.
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Use conditional statements (if, elif, else) to provide clothing recommendations
# based on the user's input.

# If the weather is "sunny", recommend appropriate clothing.
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
# Else if the weather is "rainy", recommend appropriate clothing.
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
# Else if the weather is "cold", recommend appropriate clothing.
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
# If none of the above conditions are met (i.e., unexpected input),
# provide a default message.
else:
    print("Sorry, I don't have recommendations for this weather.")
