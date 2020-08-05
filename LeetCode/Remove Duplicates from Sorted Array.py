def removeDuplicates(nums):
    n = len(nums)-1
    for i in range(1,n):
        if(nums[i] == num[i-1]):
            for j in range(i,n):
                nums[j-1] = nums[j]
    return nums

result = removeDuplicates([1,1])
print(result)
