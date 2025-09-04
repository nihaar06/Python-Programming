def fldigitsum(n):
    last=n%10
    while(n>=10):
        n=n//10
    first=n
    return first+last
n=int(input("Entee the number:"))
print("Sum of First and last digits of the number is",fldigitsum(n))