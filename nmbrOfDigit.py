number = int(input('Enter a number: '))

# A three digit number
if number >= 100 and number <= 999:
    print("The given number is a three digit number")
    
 # A four digit number
elif number >= 1000 and number <= 9999:
    print("The given number is a four digit number")   
 
else:
    print("not a 3 or 4 digit number")   