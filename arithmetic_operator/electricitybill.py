# Electricity Bill Calculation

units = 120
rate_per_unit = 8

bill_amount = units * rate_per_unit
print("Electricity Bill =", bill_amount)

tax = bill_amount * 5 / 100
total_bill = bill_amount + tax

print("Total Bill After Tax =", total_bill)