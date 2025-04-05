#find simple interest.
def si(p,r,t):
    return (p*r*t)/100
p = int(input("enter principal:"))
r = int(input("enter rate : "))
t = int(input("enter time : "))
simple_interst  = si(p,r,t)
print("simple interest is ",simple_interst)