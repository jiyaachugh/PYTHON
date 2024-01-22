num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))

operator = input("Enter the operator: ")

match operator:
    case "+":
        print("The sum is: ", num1 + num2) 
    case "-":
        print("The dfiference is: ", num1 - num2) 
    case "*":
        print("The product is: ", num1 * num2) 
    case "/":
        print("The division is: ", num1 / num2) 
    case "%":
        print("The remainder is: ", num1 % num2) 
    case "**" : 
        print("The exponent is: ", num1 ** num2)
    case "//":
        print("The division is: ", num1 // num2)
    case _ :
        print("Enter a valid operator")