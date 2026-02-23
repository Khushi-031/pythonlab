ratings = [5, 4, 3, 6, 2, 0, 5]

# Remove invalid ratings
ratings = [r for r in ratings if 1 <= r <= 5]

average = sum(ratings) / len(ratings)
print("Average Rating:", average)

print("5-Star Ratings:", ratings.count(5))

ratings.sort()
print("Sorted Ratings:", ratings)