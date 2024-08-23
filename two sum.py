arr = [-9, -7, 2, -8, -6, -6, -10, -7, -9]
arr = list(set(arr))
l = len(arr)
l_fir = list()
for i in range(0, l-1):
    for j in range(i+1, l):
        l_sec = list()
        if arr[i] + arr[j] == 0:
            l_sec.append(arr[i])
            l_sec.append(arr[j])
            l_sec.sort()
            l_fir.append(l_sec)
            l_fir.sort()
print((l_fir))