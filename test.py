#reuest user to input two integers and an operator
num1 = int(input("Enter num1: " ""))
num2 = int(input("Enter num2: " ""))
operator = input("Enter operator (+,-,*,/): " "")

#manipulating the user input to perform arithmetic operations
if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    print("The difference is:", num1 - num2)  
elif operator == "*":
    print("The multiplication is:", num1 * num2)
elif operator == "/":
#cheking to avoid zero division error    
    if num1 == 0 or num2 ==0:
        print("cant divide by zero") 
    else:      
        print("The division is:", num1 / num2)
else:
    print("Invalid operator")

