def addele():
    l=[]
    while True:
        x=int(input("Enter the element to be added into the list :"))
        l.append(x)
        f=int(input("Do you want to continue(0 to stop) :"))
        if f==0:
            return l
def unique(l):
    return list(set(l))
l=addele()
print("The unique elements int the list are:",unique(l))