def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
def is_strong(n):
    check=n
    s=0
    while(n>0):
        s=s+factorial(n%10)
        n=n//10
    if s==check:
        return True
    else:
        return False
    
n=int(input("Enter the value of n: "))
for i in range(1,n+1):
    if(is_strong(i)):
        print(i,end=" ")