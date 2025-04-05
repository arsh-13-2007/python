count_india = 0
count_russia = 0
count_amercia = 0
dict = {
    "ram" : "india",
    "sham" : "america",
    "arsh" : "india",
    "rohit" : "russia",
    "sachin" : "america",
}
print(dict.keys())
for i in set(dict.values()):
    print(i)
print(dict.items())
for i in dict.values():

    if (i == "india"):
        count_india += 1
    elif(i == "russia"):
        count_russia += 1
    else:
        count_amercia += 1
print("from india:",count_india)
print("from russia:",count_russia)
print("from amercia:",count_amercia)
