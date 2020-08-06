def removeDuplicates(nums):
    result = []
    length = 1;
    if(len(nums)==0):
        return 0
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            result.append(nums[i])
            length += 1
    return result

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
