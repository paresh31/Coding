s = "abbaca"
l = []
for c in s:
    if l and l[-1] == c:
        l.pop()
    else:
        l.append(c)
print(l)
    