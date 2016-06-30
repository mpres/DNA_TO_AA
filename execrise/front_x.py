def front_x(words):
    xlst = []
    lst = []
    for a in words:
        if a[0] == "x" or a[0] == "X":
            xlst.append(a)
        else:
            lst.append(a)
    lst.sort()
    lst2 = xlst + lst
    return  lst2

l1 = ["abc","xyz","bbb","xex","zel","ccc",'yyy','xox']
print front_x(l1)
