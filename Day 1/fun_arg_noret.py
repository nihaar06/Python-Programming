def days_to_yrs_mnths(d):
    yr=d/365
    mnth=d//30
    print("Years and months :",round(yr,2),",",round(mnth,2))
days=int(input("Enter the number of days: "))
days_to_yrs_mnths(days)