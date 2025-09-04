def checkchar(c):
    if c.isalpha():
        return "Alphabet"
    elif c.isdigit():
        return "Digit"
    else:
        return "Special Character"
c=input("Enter a character: ")
print("The character is",checkchar(c))