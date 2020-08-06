def removeElement(nums, val):
    pointer2 = 0
    for pointer1 in range(len(nums)):
        if nums[pointer1] != val:
            nums[pointer2] = nums[pointer1]
            pointer2 += 1
    return pointer2

print(removeElement([0,1,2,2,3,0,4,2],2))
