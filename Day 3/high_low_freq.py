def count_frequency(l):
    f={}
    for i in l:
        if i in f:
            f[i]+=1
        else :
            f[i]=1
    return f
def high_low_freq(f):
    max=-1
    min=float('inf')
    for i in f:
        if f[i]>max:
            max=f[i]
        if f[i]<min:
            min=f[i]
    return max,min
s=input("Enter a string: ")
print(count_frequency(s))
h,l=high_low_freq(count_frequency(s))
print("Highest Frequency: ",h,"\nLowest Frequency: ",l)