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
l=addele()
f=count_frequency(l)
for i in f:
    print(i,"->",f[i])