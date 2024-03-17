num1=input("Enter a val:")
num2=input("Enter another val:")
print("Original pair:"+num1+','+num2)
temp=num1
def swap(a,b):
    a=b
    b=temp
    print("swaped pair:" + a +','+b)
swap(num1,num2)

     

