scores = [25, 30, 32, 45, 50, 28, 60]

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

# Add grace marks
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

# Count passed students
passed = 0
for s in scores:
    if s >= 40:
        passed += 1

print("Passed Students:", passed)