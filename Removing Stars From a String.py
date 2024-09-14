s = "leet**cod*e"
l = list(s)
r = []
i = 0
while i < (len(l)):
    if l[i] == "*":
        if r:
            r.pop()
    else:
        r.append(l[i])
    i += 1
print(r)