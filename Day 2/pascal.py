def pascals(n):
    triangle=[]
    for i in range(n):
        row=[1]*(i+1)
        for j in range(1,i):
            row[j]=triangle[i-1][j-1]+triangle[i-1][j-1]
        triangle.append(row)
    return triangle
n=int(input("Enter the value of n: "))
for row in pascals(n):
    print(row)