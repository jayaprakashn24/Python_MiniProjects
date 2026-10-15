


num1 = float(input("First number: "))
num2 = float(input("Second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    print("Result:", num1 / num2 if num2 != 0 else "Cannot divide by zero")
else:
    print("Invalid operator")
    

