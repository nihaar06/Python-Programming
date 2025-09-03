def checkvc(c):
    if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
        return "Character is a Vowel"
    else:
        return "Not a vowel"
c=input("Enter a character: ")
print(checkvc(c))