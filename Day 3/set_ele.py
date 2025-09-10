def add_ele():
    s=set()
    while True:
        y=input("Enter the element to be inserted into the set: ")
        s.update(y)
        f=input("Do you want to continue? (yes/no)")
        if f.lower()!='yes':
            return s
print("The set is: ",add_ele())