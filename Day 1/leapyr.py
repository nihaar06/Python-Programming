def leap(yr):
    if(yr%4==0):
        if(yr%100==0):
            if(yr%400==0):
                return "Leap year"
            else:
                return "Not a leap year"
        else:
            return "Leap year"
    else:
        return "Not a leap year"
yr=int(input("Enter a year: "))
print(leap(yr))