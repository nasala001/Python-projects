
# Create a calculator
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

print("Choose the arithmetic operation:")
print("Options: sum, multiply, division, exponent, floordiv")

operation = input("Enter operation: ")

if operation == "sum":
    result = n1 + n2
    print("The sum is", result)

elif operation == "multiply":
    result = n1 * n2
    print("The multiplication is", result)

elif operation == "division":
    if n2 != 0:
        result = n1 / n2
        print("The division is", result)
    else:
        print("Error: Division by zero")

elif operation == "exponent":
    result = n1 ** n2
    print("The exponent is", result)

elif operation == "floordiv":
    if n2 != 0:
        result = n1 // n2
        print("The floor division is", result)
    else:
        print("Error: Floor division by zero")

else:
    print("Invalid operation selected.")
