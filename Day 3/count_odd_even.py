def addele():
    l=[]
    while True:
        x=int(input("Enter the element to be added into the list :"))
        l.append(x)
        f=int(input("Do you want to continue(0 to stop) :"))
        if f==0:
            return l
def count_e_o(l):
    co=0
    ce=0
    for i in l:
        if i%2==0:
            ce+=1
        else:
            co+=1
    return ce,co
l=addele()
ec,oc=count_e_o(l)
print("The count of even and odd numbers in the given list is:",ec,oc)