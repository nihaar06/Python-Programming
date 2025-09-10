def addele():
    l=[]
    while True:
        x=int(input("Enter the element to be added into the list :"))
        l.append(x)
        f=int(input("Do you want to continue(0 to stop) :"))
        if f==0:
            return l
def displayneg(l):
    res=[]
    for i in l:
        if i<0:
            res.append(i)
    return res
print(displayneg(addele()))