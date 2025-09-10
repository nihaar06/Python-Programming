def apply_discount(price,discount):
    price=price-(price*discount/100)
    return price
def add_gst(price,gst_percent=18):
    return price+price*(gst_percent/100)
def generate_invoice(cart,discount_percent=0,gst_percent=18):
    uc={}
    for i in cart:
        x=apply_discount(cart[i],discount_percent)
        y=add_gst(x,gst_percent)
        uc[i]=y
        print(i,':',uc[i])
    return uc