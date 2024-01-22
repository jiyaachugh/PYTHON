n1 = int(input("enter a number: "))
n2 = int(input("enter another number: "))
n3 = int(input("enter one more number: "))

#if n1 is greatest of all
if n1 > n2  and n1 > n3:
    print("n1 is the greatest of the three")
    
#if n2 is greatest of all
elif n2 > n1  and n2 > n3:
    print("n2 is the greatest of the three")
    
else: print("n3 is the greatest among the three")    