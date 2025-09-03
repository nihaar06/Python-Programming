def max(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
a,b,c=map(int,input("Enter three numbers: ").split())
print(f"Maximum of {a},{b},{c} is {max(a,b,c)}")