# Electricity Bill Calculator

units = float(input("Enter units consumed: "))
senior = input("Are you a senior citizen? (yes/no): ")

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (200 * 7) + (units - 300) * 10

if senior.lower() == "yes":
    bill = bill * 0.90   # 10% discount

print("Total Electricity Bill =", bill)
