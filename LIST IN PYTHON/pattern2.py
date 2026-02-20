n=int(input("enter no of rows"))
if n>0:
    for rows in range(1,n+1):
        print(" "*(n-rows)+ "*"*rows)
else:
    print("not possible to print")
    