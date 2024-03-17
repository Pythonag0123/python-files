year=int(input("Enter The year:"))
if year%400==0 and year%100==0:
    print("Yes")
elif year%4==0 and year%100!=0:
    print("Yes")
else:
    print("No")