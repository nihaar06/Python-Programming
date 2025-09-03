def divby5_11(n):
    if(n%5==0 and n%11==0):
        return "The number is divisible by both 5 and 11"
    else:
        return "The number is not divisible by 5 and 11"
n=int(input("Enter a number: "))
print(divby5_11(n))