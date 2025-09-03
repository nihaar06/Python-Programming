def checkalp(c):
    if(c>='A' and c<='Z') or (c>='a' and c<='z'):
        return "Character is an Alphabet"
    else:
        return "Not an alphabet"
c=input("Enter a character: ")
print(checkalp(c))