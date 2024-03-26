#factorial using built-in fucntion
import math
n=int(input("Enter the number:"))
result=math.factorial(n)
print(result)
#factorial using recursion function
def fact(m):
    if m==0:
        return 1
    else:
        return m*fact(m-1)
print(fact(n))
#Factorial using loop
fac=1
while n>0:
    fac*=n
    n-=1
print(fac)

