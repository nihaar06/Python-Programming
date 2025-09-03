def evenodd(n):
    if(n%2==0):
        return "Even"
    else:
        return "Odd"
n=int(input("Enter a number: "))
print("The number is",evenodd(n))