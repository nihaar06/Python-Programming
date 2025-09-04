def isperfect(n):
    s=0
    check=n
    for i in range(1,int(n/2)+1):
        if(n%i)==0:
            s=s+i
    if s==check:
        return True
    else:
        return False
n=int(input("Enter the value of n: "))
for i in range(1,n+1):
    if isperfect(i):
        print(i,end=" ")