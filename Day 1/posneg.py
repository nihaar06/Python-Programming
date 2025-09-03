def posneg(n):
    if n>0:
        return "Positive"
    else:
        return "Negative"
n=int(input("Enter a number: "))
print("The number is",posneg(n))