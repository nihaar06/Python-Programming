def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter the value of n: "))
for i in range(n+1):
    print(fib(i))