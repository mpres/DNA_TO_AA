import sys
import os
def print_words(filename):
    f = open(filename,"r")
    s = f.read()
    lst = s.split()
    lst = [x.lower() for x in lst]
    ulst = list(set(lst))    
    d = {}

    for a in ulst:
        d[a] = lst.count(a)
    d1 =  sorted(d)
    result = []
    for b in d1:  
        result.append(str(b)+ ' ' + str(d[b]))  
    return "\n".join(result)




def print_top(filename):
    f = open(filename,"r")
    s = f.read()
    lst = s.split()
    lst = [x.lower() for x in lst]
    ulst = list(set(lst))    
    d = {}

    for a in ulst:
        d[a] = lst.count(a)
    d1 =  sorted(d,key=d.get, reverse=True)
    result = []
    for b in d1:
        result.append(str(b)+ ' ' + str(d[b]))
    result = result[:8]
    #print result
    return "\n".join(result)


#print print_words("Test.txt")
print print_top("Test.txt")


