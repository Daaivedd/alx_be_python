num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
the_type =input("Choose the operation (+, -, *, /): ")
x = True
match the_type :
    case  ("+") :
        result = num1 + num2
    case  ("-") :
        result = num1 - num2
    case  ("*") :
        result = num1 * num2
    case  ("/") :
        if num2 == 0 :
            x = False
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
if x == True :
    print(f"The result is {result}")