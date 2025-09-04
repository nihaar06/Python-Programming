def pass_or_fail(m,p,c):
    if m>40 and p>40 and c>40:
        return "Pass"
    else:
        return "Fail"
def grade(m,p,c):
    avg=(m+p+c)/3
    if avg<50:
        return "C"
    elif avg>=51 and avg<=70:
        return "B"
    elif avg>=71 and avg<=80:
        return "A"
    else:
        return "Distinction"
sname=input("Enter the name of the student:")
sno=int(input("Enter the roll number of the student:"))
m=int(input("Enter the maths marks: "))
p=int(input("Enter the physics marks: "))
c=int(input("Enter the chemistry marks: "))
print("Details of the student are: ")
print("Name :",sname,"\nRoll Number :",sno,"\nMath marks: ",m,"\nPhysics marks: ",p,"\nChemistry marks: ",c)
print("Result :",pass_or_fail(m,p,c))
print("Total marks: ",m+p+c)
print("Average marks: ",round((m+p+c)/3,2))
if(pass_or_fail(m,p,c)=="Pass"):
    print("Grade :",grade(m,p,c))