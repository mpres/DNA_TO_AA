def donuts(count):
    if count < 10:
        s = "Number of donuts: %d" % (count)
    else:
        s = "Number of donuts: many"
    return s

print donuts(8)
