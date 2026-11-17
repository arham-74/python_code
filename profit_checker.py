cost_price = float(input("Enter the cost price: "))
sell_price = float(input("Enter the selling price: "))

if sell_price > cost_price:
    profit = sell_price - cost_price
    print("The total profit is: {0:.2f}".format(profit))
else:
    print("NO PROFIT!!")