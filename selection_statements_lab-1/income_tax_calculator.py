# Income Tax Calculator (India Based)

income = float(input("Enter annual income: "))
age = int(input("Enter age: "))

if age >= 60:
    exemption = 300000
else:
    exemption = 250000

if income <= exemption:
    tax = 0
elif income <= 500000:
    tax = (income - exemption) * 0.05
elif income <= 1000000:
    tax = (income - 500000) * 0.20 + (500000 - exemption) * 0.05
else:
    tax = (income - 1000000) * 0.30 + 500000 * 0.20 + (500000 - exemption) * 0.05

print("Income Tax =", tax)
