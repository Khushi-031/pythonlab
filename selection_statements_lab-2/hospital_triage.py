# Hospital Emergency Triage

age = int(input("Enter age: "))
heart_rate_abnormal = input("Is heart rate abnormal? (yes/no): ")
severe_injury = input("Severe injury? (yes/no): ")

if heart_rate_abnormal.lower() == "yes" or severe_injury.lower() == "yes":
    print("Category: Critical")
else:
    condition = input("Condition (moderate/normal): ")
    
    if condition.lower() == "moderate" and age > 65:
        print("Category: Critical (Upgraded due to age)")
    elif condition.lower() == "moderate":
        print("Category: Moderate")
    else:
        print("Category: Normal")
