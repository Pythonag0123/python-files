n=int(input("Enter number you want to check:"))
count=0
for i in range (2,n+1):
    if n%i==0:
        count+=1
    else:
        pass
if count<=2:
    print(str(n) + "is a prime number")
else:
    print(str(n) + "is not a prime number")