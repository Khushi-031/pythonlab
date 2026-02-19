# Salary Increment System

rating = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

if rating >= 4 and experience >= 5 and attendance >= 90:
    increment = 15
elif rating >= 3 and attendance >= 80:
    increment = 10
else:
    increment = 5

print("Increment Percentage =", increment, "%")
