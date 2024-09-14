n = 5
l = []
for i in range(n+1):
    a = bin(i)[2:]
    count = 0
    for ele in a:
        if ele == '1':
            count += 1
    l.append(count)
print(l)