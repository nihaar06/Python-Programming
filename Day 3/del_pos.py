def addele():
    l=[]
    while True:
        x=int(input("Enter the element to be added into the list :"))
        l.append(x)
        f=int(input("Do you want to continue(0 to stop) :"))
        if f==0:
            return l
def delpos(l,pos):
    if pos<0 or pos>len(l):
        print("Invalid position")
    else:
        return l[:pos]+l[pos+1:]
print("The list after deleting the element at the given position is:",
      delpos(addele(),int(input("Enter the position to be deleted (pos>0):"))))