import math
def hypo(base , perp):
    hypo = (base*base) + (perp*perp)
    return math.sqrt(hypo)
base = int(input("enter base : "))
perp = int(input("enter  perpendicular : "))
hypotenuse=hypo(base ,  perp)
print("hypotenuse is : ", hypotenuse)