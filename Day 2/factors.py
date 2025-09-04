def printfactors(n):
    for i in range(1,n//2+1):
        if(n%i==0):
            print(i,end=" ")
n=int(input("Enter the value of n: "))
printfactors(n)