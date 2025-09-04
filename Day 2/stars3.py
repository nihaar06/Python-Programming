def printstars3(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==j or j==n-i+1):
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()
n=int(input("Enter the number of rows: "))
printstars3(n)