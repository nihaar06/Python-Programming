def count_vow_cons(s):
    vowels="aeiouAEIOU"
    v=0
    c=0
    for i in s:
        if i in vowels:
            v+=1
        else:
            c+=1
    return v,c
s=input("Enter the string: ")
print("In the string, the count of vowels :",count_vow_cons(s)[0],",the count of consonants :",count_vow_cons(s)[1])