def calc_bill(tu):
    if(tu<=50):
        return tu*3.80
    elif(tu>50 and tu<=100):
        return (50*3.80)+(tu-50)*4.20
    elif(tu>100 and tu<=200):
        return (50*3.80)+(50)*4.20+(tu-100)*5.10
    elif(tu>200 and tu<=300):
        return (50*3.80)+(50)*4.20+(100)*5.10+(tu-200)*6.30
    else:
        return (50*3.80)+(50)*4.20+(100)*5.10+100*6.30+(tu-300)*7.50
cno=int(input("Enter the consumer number:  "))
cname=input("Enter the consumer name: ")
pmr=float(input("Enter the present month reading: "))
lmr=float(input("Enter the last month reading: "))
tu=pmr-lmr
bill=calc_bill(tu)
print("***CONSUMER DETAILS***")
print("Consumer no.: ",cno,"\nConsumer name: ",cname,"\nPresent month reading: ",pmr,"\nLast month reading: ",lmr,"\nTotal units consumed: ",tu,"\nBill amount: ",bill)