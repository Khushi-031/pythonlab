transactions = [20000, -5000, 15000, -2000, 8000]

balance = sum(transactions)
print("Total Balance:", balance)

# Largest withdrawal
withdrawals = [t for t in transactions if t < 0]
print("Largest Withdrawal:", min(withdrawals))

# Deposits > 10000
count = 0
for t in transactions:
    if t > 10000:
        count += 1

print("Deposits > 10000:", count)