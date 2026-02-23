marks=[95,102,65,-7,87,90,76,150,90]
#remmove invalid ones
valid_marks=[]
for m in marks:
    if 0<=m<=100:
        valid_marks.append(m)
    #calculate average 
average=sum(valid_marks)/len(valid_marks)
print("average marks",average)
#find topper
top=max(valid_marks)
print("topper is :",top)
#grade based on average
if average >=90:
    grade ="A"
elif average >=75:
    grade ="B"
elif average >=50:
    grade="C"
else:
    grade ="D"
print("Grade : ",grade)
