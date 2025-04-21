print("Welcome to our calculator")

num1 = float(input("\n Enter your fist number: " ))
num2 = float(input("\n Enter your second number: "))

operator = input("\n Pick an operator: +, -, *, / ")

if operator == '+':
    print("Result is " + str(num1 + num2))
elif operator == '-':
    print("Result is " + str(num1 - num2))
elif operator == '*':
    print("Result is " + str(num1 * num2))
elif operator == '/':
    if num2 != 0:
        print("Result is " + str(num1 / num2))
    else:
        print("Error- division by zero")


