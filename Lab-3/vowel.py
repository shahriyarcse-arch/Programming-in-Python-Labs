ch = input("Enter a character: ").lower()

vowels = ['a', 'e', 'i', 'o', 'u']

if ch in vowels:
    print(f"'{ch}' is a vowel.")
else:
    print(f"'{ch}' is not a vowel.")
