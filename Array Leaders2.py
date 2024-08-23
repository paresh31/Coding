class Solution:
    # Function to find the leaders in the array.
    def leaders(self, n, arr):
        l = []
        last = arr[-1]
        l.append(last)
        for i in range(n-2, -1, -1):
            if arr[i] >= last:
                l.append(arr[i])
                last = arr[i]
        l.reverse()
        return l