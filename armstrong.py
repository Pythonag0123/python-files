#armstrong number
#logic-sare digits ke cube ka sum at the end bahi number aaye
n=input("Enter the number to check:").strip()
sum=0
for i in n:
    sum+=(int(i))**3
if sum==int(n):
    print("Yes")
else:
    print("No")
