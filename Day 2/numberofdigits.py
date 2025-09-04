def numberofdigits(n):
    c=0
    while(n>0):
        c=c+1
        n=n//10
    return c
n=int(input("Enter the number: "))
print(f"The number of digits in {n} is {numberofdigits(n)}")