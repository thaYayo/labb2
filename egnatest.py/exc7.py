# You are interested in buying a new laptop. You check the price and you see that the price is 300$ without the 10% tax.

# Create a program that:

# Reads the price of the laptop
# Reads the tax percentage
# Prints the total amount
# Output: "The total price of the laptop is 330$"

price = 300
tax = 10

percentage = price/100 * tax
total = price + percentage

print(f"The total price is {total}$")
