# You've bought a Bitcoin and now it's on the rise!!!

# Create a program that:

# Reads the value of the bitcoin at the time of purchase
# Reads the percentage of increase (or decrease)
# Prints the total value of your bitcoin
# Prints the increase or decrease value
# Example: bitcoin_value = 10000, bitcoin_increase = 10
# Output: total_bitcoin_value = 11000, bitcoin_increase_value = 1000

bitcoin_valuepurchase = 10000
bitcoin_increase = 1000
total_value = bitcoin_increase + bitcoin_valuepurchase

# percentage lambda
##p = lambda x,y: (x/y) * 100

change_percentage = bitcoin_increase/total_value *100

def bitcoin():
    print(f"The total value: {total_value}, Change in percentage: {change_percentage}")

bitcoin()

