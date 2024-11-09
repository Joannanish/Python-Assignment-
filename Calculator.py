num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

operation = input("Enter your choice (1/2/3/4): ")

if operation == '1':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operation == '2':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif operation == '3':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid input! Please choose a valid operation.")
