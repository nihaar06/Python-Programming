def fldigit(n):
    last=n%10
    while(n>=10):
        n=n//10
    first=n
    return first,last
n=int(input("Entee the number:"))
print("First and last digits of the number is",fldigit(n)[0],"and",fldigit(n)[1])