#creating a blank list
numbers=[]
#take number of elements
n=int(input("enter number of elements"))
#ask for elements
for i in range(n):
    num=int(input("enter a  number"))
    print("----------------")
    numbers.append(num)
print("numbers are: ",numbers)
sum=0
for num in numbers:
    sum =sum+num
print(sum)