#armstrong number
#logic-tottal number of digits jitne hain , har digit ki utni power ka sum bpas bahi number aaye to it's armstrong number else: not
num=int(input("Enter number to check:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=(digit)**len(str(num))
    temp=temp//10
if sum==num:
    print("Yes")
else:
    print("No")
    
    
    
