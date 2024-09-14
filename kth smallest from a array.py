# arr = [7, 10, 4, 3, 20, 15]
# k = 4
# for i in range(k-1):
#     arr.remove(min(arr))
# print(min(arr))
    
arr = [7, 10, 4, 3, 20, 15]
k = 3
low = 0
high = len(arr) - 1
k_index = k - 1
while low <= high:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    pivot_index = i + 1
    if pivot_index == k_index:
        print(arr[pivot_index])
        break
    elif pivot_index > k_index:
        high = pivot_index - 1
    else:
        low = pivot_index + 1
