# University Admission Eligibility

percentage = float(input("Enter 12th percentage: "))
maths = input("Did you study Mathematics? (yes/no): ")
entrance = int(input("Enter entrance exam score: "))

if percentage < 75:
    print("Rejected: Minimum 75% required")
elif maths.lower() != "yes":
    print("Rejected: Mathematics is compulsory")
elif entrance < 80:
    print("Rejected: Entrance score must be ≥ 80")
else:
    print("Admission Approved")
