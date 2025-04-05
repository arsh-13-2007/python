import cmath

def quadratic_roots(a, b, c):
   
    discriminant = b**2 - 4*a*c
    
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
  
    if discriminant > 0:
        print("The equation has real and distinct roots:")
    elif discriminant == 0:
        print("The equation has real and equal roots:")
    else:
        print("The equation has imaginary roots:")
    
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

quadratic_roots(a, b, c)