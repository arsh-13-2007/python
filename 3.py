def pss(n):
    table=""
    for i in range (1 , 11):
        table += f"{n} X {i} = {n * i}\n"
        print(table)
    with open(f"tables/table{n}.txt", "w")as f: # this is way to open file through folder
        f.write(table)

for i in range(2 , 21):
    pss(i) 