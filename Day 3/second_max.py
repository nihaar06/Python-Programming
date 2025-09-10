def addele():
    l=[]
    while True:
        x=int(input("Enter the element to be added into the list :"))
        l.append(x)
        f=int(input("Do you want to continue(0 to stop) :"))
        if f==0:
            return l
def second_max(l):
    max=float('-inf')
    sec_max=float('-inf')
    for i in l:
        if i>max:
            sec_max=max
            max=i
        elif i>sec_max and i!=max:
            sec_max=i
    return sec_max
print("The second maximum element is :",second_max(addele()))