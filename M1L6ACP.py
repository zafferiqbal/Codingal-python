character = input("Enter a character: ")

if (character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z'):
    print(f"The character '{character}' is an alphabet.")
else:
    print(f"The character '{character}' is not an alphabet.")