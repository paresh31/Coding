def equilibriumPoint(arr):
    n = len(arr)
    if n == 1:
        return 1
    sum = 0
    for i in range(0, n):
        sum += arr[i]
    left_sum = 0
    for i in range(0, n):
        sum -= arr[i]
        if sum == left_sum:
            return i + 1
        left_sum += arr[i]
    return -1


arr = [1, 3, 5, 2, 2]
res = equilibriumPoint(arr)
print(res)
