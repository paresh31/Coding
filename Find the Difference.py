s = "abc"
t = "abcd"
a = list(s)
b = list(t)
for c in a:
    if c in b:
        b.remove(c)
print(b)
    
