name = input("Enter your name: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

total = num1 + num2
product = num1 * num2

print(f"\nHello, {name}!")
print("Variable 'name' type:", type(name))
print(f"Sum of {num1} and {num2}: {total}")
print(f"Product of {num1} and {num2}: {product}")
