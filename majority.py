def majorityElement(nums):
    n = list()
    for i in range(len(nums)):
        n.append(nums.count(nums[i]))
    print(n)
    m = max(n)
    cri = len(nums)//2
    c = n.count(m)
    print(f'cri: {cri} c: {c}')
    if c > cri:
        x = nums[n.index(m)]
        print(x)
    else:
        print(-1)




nums = [1,13,8,23,4,5]
print(majorityElement(nums))