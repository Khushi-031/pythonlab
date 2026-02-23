stock = [0, 5, 20, 8, 15, 0]

# Remove zero stock
stock = [s for s in stock if s != 0]

# Restock items below 10
for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

total_inventory = sum(stock)

print("Total Inventory:", total_inventory)