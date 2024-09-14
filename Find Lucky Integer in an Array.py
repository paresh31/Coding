arr = [1,2,2,3,3,3]
l = [-1]
for i in range(len(arr)):
    if arr[i] == arr.count(arr[i]):
        l.append(arr[i])
print(max(l))