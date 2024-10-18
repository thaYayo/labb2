# You are interested in buying crypto-currencies. You want to check the current amount of money you have and see how many coins you can buy in Bitcoin, Ethereum, and Litecoin.

# Create a program that:

# Reads the total amount of money you have
# Reads the price of Bitcoin, Ethereum, and Litecoin
# Prints the amount of Bitcoin, Ethereum, and Litecoin you can buy
# Example: money = 100, bitcoin_price = 50, ethereum_price = 25, litecoin_price = 10
# Output: "With 100$ you can buy: 2 Bitcoins, 4 Ethereum, and 10 Litecoins"
# (Warning! Τhe prices are made up for exercise purposes)

Bitcoin = 60000
Ethereum = 4000
Litecoin = 2000

money = float(input("Enter the amount of money you have: "))

def buy():
    if money >= Litecoin and money < Ethereum:
        print("You have enough money to buy 1 Litecoin!")
    if money >= Ethereum and money < Bitcoin:
        print("You have enough money to buy 1 Eth or 2 Litecoins!")
    if money >= Bitcoin:
        print("You have enough money to buy 1 Btc!")
    if money < Litecoin:
        print("You do not have enough money to buy any coin!")
    

buy()

