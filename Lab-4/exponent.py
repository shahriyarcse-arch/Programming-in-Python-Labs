base = float(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = 1
for i in range(abs(exp)):
    result *= base

if exp < 0:
    result = 1 / result

print(f"{base} ^ {exp} = {result}")
