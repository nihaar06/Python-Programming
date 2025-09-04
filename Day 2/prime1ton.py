from math import sqrt
def prime1ton(n):
    for i in range(2,n):
        f=0
        for j in range(2,int(sqrt(i))+1):
            if i%j==0:
                f=1
                break
        if f==0:
            print(i)
n=int(input("Enter the value of n:"))
print("Prime numbers in the range of 1 to",n)
prime1ton(n)