n=int(input("enter rows"))
if n>0:
    for rows in range(1,n+1):
        print(" "*(n-rows)+"*"*(2*rows-1))
    for rows in range(n-1,0,-1):
        print(" "*(n-rows)+"*"*(2*rows-1))

else:
    print("not possible")