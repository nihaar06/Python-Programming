def sumofdigits(n):
    s=0
    while(n>0):
        s=s+n%10
        n=n//10
    return s
n=int(input("Enter the number :"))
print("The sum of digits is:",sumofdigits(n))