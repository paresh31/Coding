arr = [2, 1, 6]
brr = [1, 5]
c = 0
for i in range(len(arr)):
    for j in range(len(brr)):
        if arr[i]**brr[j] > brr[j]**arr[i]:
            c += 1
print(c)