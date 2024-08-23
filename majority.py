def majorityElement(nums):
    n = list()
    for i in range(len(nums)):
        n.append(nums.count(nums[i]))
    m = max(n)
    x = nums[n.index(m)]
    return x




nums = [2,2,1,1,1,2,2,3,3,3,3,1,1,1,1,1,5,6,8,7,9,5,4,5,1,1,1,1,1,1,5,4,8,9,6,5,5,1,1,1,1,1,5,5,5,9,6,6]
print(majorityElement(nums))