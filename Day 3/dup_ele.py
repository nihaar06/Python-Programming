def addele():
    l=[]
    while True:
        x=int(input("Enter the element to be added into the list :"))
        l.append(x)
        f=int(input("Do you want to continue(0 to stop) :"))
        if f==0:
            return l
def count_frequency(l):
    f={}
    for i in l:
        if i in f:
            f[i]+=1
        else :
            f[i]=1
    return f
def count_dup(f):
    c=0
    for i in f:
        if f[i]>1:
            c+=1
    return c
l=addele()
f=count_frequency(l)
print("The count of duplicate elements in the given list is:",count_dup(f))