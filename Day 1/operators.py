def operations(a,b):
    return a+b,a-b,a*b,a/b,a%b
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("Sum :",operations(a,b)[0])
print("Difference :",operations(a,b)[1])
print("Product :",operations(a,b)[2])
print("Quotient :",operations(a,b)[3])
print("Remainder :",operations(a,b)[4])