n = 64
t = False
for i in range(n):
    if 4**i == n:
        t = True
        break
    if 4**i > n:
        break
print(t)