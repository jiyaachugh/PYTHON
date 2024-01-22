n1 = int(input("enter a number: "))
n2 = int(input("enter another number: "))
n3 = int(input("enter one more number: "))

#comparing n1 and n2
if n1 > n2:
    # either n1 or n3 will be the greatest
    if n1 > n3:
        print(n1, "is the greatest")
    else:
        print(n3, "is the greatest")
else:
    #either n2 or n3 is the greatest
    if n2 > n3:
        print(n2,"is the greatest")
    else:
        print(n3,"is the greatest")