def duplicates(n, a):
    l = list()
    for i in range(n):
        if a[i] not in l:
            c = a.count(a[i])
            if c != 1:
                l.append(a[i])
    s = len(l)
    if  s != 0:
        return l
    else:
        return -1

a = [0, 3, 1, 2]
n = len(a)
re = duplicates(n, a)
print(re)
