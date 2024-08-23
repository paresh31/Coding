nums1 = [1,3]
nums2 = [2]

nums = nums1 + nums2

print(nums)
sorted(nums)
length = len(nums)
print(f"length of the merged array is : {length}")

if length%2==0:
    median = (nums[int(length/2)] + nums[(int(length/2))-1]) /2
    print(f"median is {median}")
else:
    median = nums[int(length/2)]
    print(f"median is {median}")
    