cno=int(input("Enter the consumer number:  "))
cname=input("Enter the consumer name: ")
pmr=float(input("Enter the present month reading: "))
lmr=float(input("Enter the last month reading: "))
tu=pmr-lmr
bill=tu*3.80
print("CONSUMER DETAILS")
print("Consumer no.: ",cno,"\nConsumer name: ",cname,"\nPresent month reading: ",pmr,"\nLast month reading: ",lmr,"\nTotal units consumed: ",tu,"\nBill amount: ",bill)