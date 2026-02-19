# Input cost price and selling price
cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

# Calculate profit or loss
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit =", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss =", loss)
else:
    print("No Profit No Loss")
