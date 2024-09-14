
def removeElement(nums= [0,1,2,2,3,0,4,2], val= 2):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return nums

removeElement(nums= [0,1,2,2,3,0,4,2], val= 2)
