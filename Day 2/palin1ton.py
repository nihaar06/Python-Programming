def ispalindrome(n):
    if n==rev(n):
        return True
    else:
        return False
def rev(n):
    reverse=0
    while(n>0):
        rem=n%10
        reverse=reverse*10+rem
        n=n//10
    return reverse
n=int(input("Enter the value of n: "))
for i in range(1,n+1):
    if(ispalindrome(i)):
        print(i,end=" ")