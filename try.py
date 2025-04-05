sum_area = 0 
with open("city.txt") as f:
    for i in f:
        city , population , area = i.split()
        sum_area = sum_area + float(area)
print(f"total area is {sum_area}")
            
   
   
 
            
