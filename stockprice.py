# Predefined stock prices
stock_prices = {
    "APPLE": 1800,
    "TESLA": 2500,
    "GOOGLE": 1300,
    "AMAZON": 1400,
    "MICROSOFT": 3000
}

total_value = 0
user_data = []

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found.")
        continue
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
        value = stock_prices[stock] * qty
        total_value += value
        user_data.append((stock, qty, value))
    except ValueError:
        print("Invalid quantity. Try again.")

print("\nYour Portfolio:")
for stock, qty, value in user_data:
    print(f"{stock}: {qty} shares x rs{stock_prices[stock]} = rs{value}")

print(f"Total Investment Value: rs{total_value}")

save = input("Save to file? (yes/no): ").lower()
if save == "yes":
    with open("investment_summary.txt", "w") as f:
        for stock, qty, value in user_data:
            f.write(f"{stock},{qty},{value}\n")
        f.write(f"Total,{total_value}\n")
    print("Data saved to investment_summary.txt")
