nums = [0,1,0,3,12]
l = nums.count(0)
for i in range(l):
    nums.remove(0)
    nums.append(0)
print(nums)