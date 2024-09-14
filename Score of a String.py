s = "hello"
l = list(s)
a = list()
for item in l:
    a.append(ord(item))
s = 0
for i in range(0, len(a)-1):
    s = s + abs(a[i] - a[i+1])
print(s)