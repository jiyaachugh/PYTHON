n = int(input("Enter a number n: "))

for i in range(1,n+1): # loop for rows
    #printing spaces
    print(" " * (n-i),end = "" )
    
    #printing digits
    for j in range(1, 2 * i): #loop for columns
        print(j, end = " ")
    print()
        