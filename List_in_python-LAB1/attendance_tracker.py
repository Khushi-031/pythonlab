attendance = [1, 1, 0, 0, 1, 0, 1]

percentage = (sum(attendance) / len(attendance)) * 100
print("Attendance %:", percentage)

if percentage < 75:
    print("Warning: Below 75%")

# Replace consecutive absences with warning
for i in range(len(attendance) - 1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = "Warning"

print("Updated Attendance:", attendance)