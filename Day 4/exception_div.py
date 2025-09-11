def div():
    try:
        num=int(input("Enter the numeartor:"))
        den=int(input("Enter the denominator:"))
        res=num/den
        print("Quotient: ",res)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except:
        print("Invalid")
div()