# E-commerce Discount Engine

cart_value = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum): ")
festival = input("Is it festival season? (yes/no): ")

discount = 0

# Membership discount
if membership.lower() == "silver":
    discount = 0.05
elif membership.lower() == "gold":
    discount = 0.10
elif membership.lower() == "platinum":
    discount = 0.15

# Festival discount
if festival.lower() == "yes":
    discount = max(discount, 0.20)

final_amount = cart_value - (cart_value * discount)

print("Final Payable Amount =", final_amount)
