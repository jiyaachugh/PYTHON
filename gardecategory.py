marks = int(input("Enter your marks: "))

# marks are between 81 and 100
if marks > 80:
    print("very good")
    
# marks are between 81 and 100
elif marks > 60:
    print("good")    

# marks are between 41 and 60
elif marks > 40:
    print("average") 
    
# marks are less than 40
elif marks < 40:
    print("fail") 