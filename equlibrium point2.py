arr = [1, 3, 5, 2, 2]
l = len(arr)
x = l
for k in range(x):
    sum1, sum2 = 0, 0
    for i in range(0, k):
        sum1 = sum1 + arr[i]
    for j in range(k+1, l):
        sum2 = sum2 + arr[j]
    print(sum1, sum2, end="  --> ")
    print(arr[k], end="  --> ")
    print(arr.index(arr[k])+1)
    
    