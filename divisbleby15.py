num = int(input("enter a number whose divisibility is to check"))

#divisible by 15
if num % 15 == 0:
    print("the number is divisble by 15")
 
else:
    #checking if divisible by 3 or 5
    if num  % 3 == 0   or num % 5 == 0:
        print("the number is not divisble by 15 but divisible by 3 or 5")
    else:
        print("the number is neither divisble by 3 nor 5")   
   