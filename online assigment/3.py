def send(need , avb ):
    print(need.difference(avb))

need= {"water" , "ginger" , "sugar" , "milk"}
avb= {"water", "sugar"}
send( need , avb)