def count(s):
    cd=0
    ca=0
    cs=0
    for i in s:
        if i.isdigit():
            cd+=1
        elif i.isalpha():
            ca+=1
        else:
            cs+=1
    return cd,ca,cs
s=input("Enter the string: ")
print("In the string, the count of digits :",count(s)[0],",the count of alphabets :",count(s)[1],",the count of special characters :",count(s)[2])