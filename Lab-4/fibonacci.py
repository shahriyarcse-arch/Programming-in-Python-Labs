limit = int(input("Enter limit N: "))

a, b = 0, 1
print(f"Fibonacci numbers below {limit}:")

while a < limit:
    print(a, end=" ")
    a, b = b, a + b

print()
