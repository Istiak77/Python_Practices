operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number : "))

if operator == "+":
    result = num1+num2
    print(round(result, 3))
elif operator == "-":
    result = num1-num2
    print(round(result, 3))
elif operator == "*":
    result = num1*num2
    print(round(result, 3))
elif operator == "/":
    if num2 == 0:
        print("Math Error.")
    else:
        result = num1 / num2
        print(round(result, 3))
else:
    print(f"Invalid {operator} operator entered.")