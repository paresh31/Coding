nums = [9,6,4,2,3,5,7,0,1]
l = len(nums)
for i in range(l):
    if i in nums:
        continue
    else:
        print(i)