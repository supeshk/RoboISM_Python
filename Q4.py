def multby2(string):
    i=0
    doublestring=""
    while i < len(string):
        doublestring=doublestring + string[i]*2
        i = i+1
    return doublestring

print(multby2("now!"))