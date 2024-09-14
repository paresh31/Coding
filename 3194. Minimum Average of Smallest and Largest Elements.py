# nums = [1,9,8,3,10,5]
# a = []
# n = len(nums)
# for i in range(n//2):
#     ma = max(nums)
#     mi = min(nums)
#     avg = (ma+mi) / 2
#     a.append(avg)
#     nums.remove(ma)
#     nums.remove(mi)
# print(min(a))


nums = [1,9,8,3,10,5]
nums.sort()
n = len(nums)
l = []
for i in range(n//2):
    l.append((nums[0]+nums[-1])/2)
    nums.pop(0)
    nums.pop(-1)
print(min(l))
