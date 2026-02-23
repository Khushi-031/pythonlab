points = [10, -5, 25, 18, -2, 30]

# Replace negative with 0
points = [p if p >= 0 else 0 for p in points]

points.sort(reverse=True)

print("Winner Points:", points[0])
print("Runner-up Points:", points[1])
print("Leaderboard:", points)