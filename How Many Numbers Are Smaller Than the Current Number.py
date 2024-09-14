nums = [8,1,2,2,3]
l = []
for i in range(len(nums)):
    c = 0
    for j in range(len(nums)):
        if nums[i] > nums[j]:
            c += 1
    l.append(c)
print(l)
