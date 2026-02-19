# ATM Withdrawal System

balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM available cash: "))

if withdraw > 50000:
    print("Withdrawal exceeds daily limit (₹50,000)")
elif withdraw > balance:
    print("Insufficient Account Balance")
elif withdraw > atm_cash:
    print("ATM has insufficient cash")
else:
    print("Withdrawal Successful")
    print("Remaining Balance =", balance - withdraw)
