'''
*****
 *  *
  * *
   **
    *
'''
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    for j in range(rows):
        if i == 0 or j == rows-1 or i == j:
            print("*", end='')
        else:
            print(" ", end='')
    print()


           
