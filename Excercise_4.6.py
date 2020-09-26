


def computepay(h,r):
    
    h = float(h)  
    r = float(r)
    if h <= 40:
        return h*r
    elif h > 40:
        return (40*r + ((h-40)*r*1.5))
    else:
        return "Bad number"
    
hrs = input("Enter Hours:")
r = input("Enter rate:")

p = computepay(hrs,r)
print("Pay",p)
