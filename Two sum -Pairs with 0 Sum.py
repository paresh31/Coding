arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
lst = list()
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j] == 0:
            tl = []
            tl.append(arr[i])
            tl.append(arr[j])
            lst.append(sorted(tl))
ulst = [list(item) for item in set(tuple(pair) for pair in lst)]
print(sorted(ulst))