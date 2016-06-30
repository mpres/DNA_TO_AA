def mix_up(a, b):
    c = b[0:1]+a[1:]
    d = a[0:1]+b[1:]
    result = c+" "+d
    return result

print mix_up("test","word")
