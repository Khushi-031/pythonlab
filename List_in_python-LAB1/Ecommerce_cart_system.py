prices=[2000,1500,2000,2800,1000]
#remove duplicates ones
prices =list(set(prices))
total=sum(prices)
#apply 10%discount if total >5000
if total>5000:
    total=total*0.10
#add 18%gst
total =total*1.18
print("final payable amount ",total)