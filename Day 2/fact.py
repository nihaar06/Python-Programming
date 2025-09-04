def factorial(n):
    res=1
    while(n>0):
        res=res*n
        n=n-1
    return res
n=int(input("Enter the number: "))
print(f"Factorial of {n} is {factorial(n)}")