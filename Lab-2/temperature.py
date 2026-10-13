# Taking temperature input from user
temperature = float(input("Enter temperature in Celsius: "))

# Checking conditions using if-elif-else
if temperature > 30:
    print("It is a hot day.")
elif temperature >= 20:
    print("The weather is warm and pleasant.")
elif temperature >= 10:
    print("It is a cool day.")
else:
    print("It is a cold day.")
