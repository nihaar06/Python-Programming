from math import sqrt
def printfactors(n):
    for i in range(1,n//2+1):
        if(n%i==0 and prime(i)):
            print(i,end=" ")
def prime(n):
    i=2
    while i<=sqrt(n):
        if n%i==0:
            return False
        i=i+1
    return True
n=int(input("Enter the value of n: "))
printfactors(n)