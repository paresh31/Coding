s = "ABCDCDC"
t = "CDC"
c = 0
ls = len(s)
lt = len(t)
for i in range(ls-lt+1):
    x = ""
    for j in range(i,lt+i):
        x = x + s[j]
        if x == t:
            c += 1
print(c)