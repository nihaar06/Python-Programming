def isarmstrong(n):
    check=n
    c=0
    temp=n
    while(temp>0):
        c=c+1
        temp=temp//10
    s=0
    while(n>0):
        s=s+(n%10)**c
        n=n//10
    if s==check:
        return True
    return False
n=int(input("Enter the value of n: "))
for i in range(1,n+1):
    if isarmstrong(i):
        print(i,end=" ")