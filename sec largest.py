arr = [10,5,10]
s = set(arr)
arr2 = list(s)
arr2.sort()
a = arr2[-2]
if len(arr2) > 1:
    print(a)
else:
    print(-1)