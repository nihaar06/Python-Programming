def search_occ(s,p):
    l=[]
    for i in range(len(s)):
        if s[i]==p:
            l.append(i)
    return l
s=input("Enter the string: ")
p=input("Enter the character to be searched: ")
print("Character is found at: ",search_occ(s,p))