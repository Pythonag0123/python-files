rows = int(input("Enter the number of rows: "))
for i in range(rows):
    for j in range(i + 1):
        if j == 0 or i == rows - 1 or i == j:
            print("*", end='')
        else:
            print(" ", end='')
    print()
