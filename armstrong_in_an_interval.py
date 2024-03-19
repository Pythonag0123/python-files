num = int(input("Enter the range:"))
for i in range(num + 1):
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if sum == i:
        print(i)
