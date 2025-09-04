def printstars1(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("*",end=" ")
        print()
n=int(input("Enter the number of rows: "))
printstars1(n)