#Pattern Program
'''output-1
          1 2
          1 2 3
          1 2 3 4
          1 2 3 4 5'''

rows=int(input("Enter the number of the rows:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
'''output-1
          2 2
          3 3 3
          4 4 4 4
          5 5 5 5 5'''
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end='')
    print()
    
 
        
