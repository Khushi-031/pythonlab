salaries = [30000, 55000, 70000, 25000, 90000]

# Remove below minimum wage (30000)
salaries = [s for s in salaries if s >= 30000]

# Add 5% bonus to salary > 50000
for i in range(len(salaries)):
    if salaries[i] > 50000:
        salaries[i] *= 1.05

# Sort descending
salaries.sort(reverse=True)

print("Top 3 Salaries:", salaries[:3])