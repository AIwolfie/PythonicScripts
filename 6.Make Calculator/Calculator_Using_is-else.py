number1 = int(input("Enter the value 1: "))
number2 = int(input("Enter the value 2: "))
operator = input("ENter the operator (+,-,*,/): ")

if operator == "+":
    print(number1+number2)
elif operator == "-":
    print(number1-number2)
elif operator == "*":
    print(number1*number2)
elif operator == "/":
    print(number1/number2)
else:
    print("Invalid operator")