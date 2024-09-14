# nums = [10, 3, 5, 6, 2]
# l = list()
# for j in range(len(nums)):
#     c = 1
#     temp = list()
#     temp = nums.copy()
#     temp.remove(temp[j])
#     for i in range(len(temp)):
#         c = c * temp[i]
#     l.append(c)
# print(l)

nums = [10, 3, 5, 6, 2]
n = len(nums)
p = [1] * n
s = [1] * n
for i in range(1, n):
    p[i] = p[i - 1] * nums[i - 1]
for i in range(n - 2, -1, -1):
    s[i] = s[i + 1] * nums[i + 1]
a = [p[i] * s[i] for i in range(n)]
print(a)
    
    
    


