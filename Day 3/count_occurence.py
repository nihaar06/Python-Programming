def count_occurence(s):
    c=1
    res='' 
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            c+=1
        else:
            res=res+s[i]+str(c)
            c=1
    res=res+s[len(s)-1]+str(c)
    return res
s=input("Enter a string: ")
print("The occurence of the string is:",count_occurence(s))