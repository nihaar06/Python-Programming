p=int(input("Enter the principal amount: "))
t=int(input("Enter the time in months: "))
r=int(input("Enter the rate of interest: "))
si=(p*t*r)/100
total=p+si
print("Simple Interest :",si)
print("Total Amount :",total)