def ntow(n):
    dic=["zero","one","two","three","four","five","six","seven","eight","nine"]
    s=""
    while(n>0):
        s=dic[n%10]+" "+s
        n=n//10
    return s
n=int(input("Enter the number:"))
print("Number in words is :",ntow(n))