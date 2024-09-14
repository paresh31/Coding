arr = [5, 5, 4, 6, 4]
l = []
for i in range(len(arr)):
    l.append(arr.count(arr[i]))
print(l)