def sortit(list1,string):
    if string == "asc":
        list1.sort()
        return list1
    elif string == "desc":
        list1.sort(reverse=True)
        return list1
    elif  string != "none":
        return "Invalid Argument"

print(sortit([5,4,7,8,2],"desc"))