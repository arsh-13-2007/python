def table():
    print("x y x&y x|y x^y")
    for x in [0, 1]:
        for y in [0, 1]:
            print(f"{x} {y}  {x&y}   {x|y}  {x^y}")
table()