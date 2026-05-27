# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_value = 0

print("=== Stock Portfolio Tracker ===")

# Number of stocks
num = int(input("Enter number of stocks: "))

# Loop for stock entries
for i in range(num):

    stock_name = input("\nEnter stock name (AAPL/TSLA/GOOG/MSFT): ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        stock_value = stock_prices[stock_name] * quantity

        total_value += stock_value

        print("Investment Value of", stock_name, "= $", stock_value)

    else:
        print("Stock not found!")

# Final portfolio value
print("\nTotal Portfolio Value = $", total_value)

# Save to file option
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save == "yes":

    file = open("portfolio.txt", "w")

    file.write("Total Portfolio Value = $" + str(total_value))

    file.close()

    print("Result saved successfully in portfolio.txt")

else:
    print("Program Ended")
