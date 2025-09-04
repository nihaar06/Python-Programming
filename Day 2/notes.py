def number_of_notes(n):
    total_notes=0
    while(n>0):
        if n>=2000:
            total_notes+=n/2000
            n=n%2000
        elif n>=500:
            total_notes+=n/500
            n=n%500
        elif n>=200:
            total_notes+=n/200
            n=n%200
        elif n>=100:
            total_notes+=n/100
            n=n%100
        elif n>=50:
            total_notes+=n/50
            n=n%50
        elif n>=20:
            total_notes+=n/20
            n=n%20
        elif n>=10:
            total_notes+=n/10
            n=n%10
        elif n>=5:  
            total_notes+=n/5
            n=n%5   
        elif n>=2:
            total_notes+=n/2
            n=n%2
        elif n>=1:
            total_notes+=n/1
            n=n%1
    return int(total_notes)
n=int(input("Enter the amount: "))
print("The number of notes required are: ",number_of_notes(n))