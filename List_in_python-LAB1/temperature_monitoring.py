temps = [35, 42, 46, 39, 44, 50]

print("Hottest Day:", max(temps))
print("Coldest Day:", min(temps))

extreme_days = 0

for i in range(len(temps)):
    if temps[i] > 45:
        temps[i] = "Heat Alert"
    if type(temps[i]) == int and temps[i] > 40:
        extreme_days += 1

print("Extreme Days (>40):", extreme_days)
print("Updated Temps:", temps)