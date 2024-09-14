n,m = 1,10
l = []
for i in range(n,m+1):
    c = 0
    for j in range(1,i):
        if i % j == 0:
            c+=1 
    if c == 1:
        l.append(i)
print(l)