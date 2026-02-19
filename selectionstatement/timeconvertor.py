# Time Converter with Options

print("1. Hours to Minutes")
print("2. Hours to Seconds")
print("3. Minutes to Seconds")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    hours = float(input("Enter hours: "))
    print("Minutes =", hours * 60)

elif choice == 2:
    hours = float(input("Enter hours: "))
    print("Seconds =", hours * 3600)

elif choice == 3:
    minutes = float(input("Enter minutes: "))
    print("Seconds =", minutes * 60)

else:
    print("Invalid choice")
