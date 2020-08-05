def findDisappearedNumbers(nums):
    n = len(nums)
    for i in range(n):
        absoluteValue = abs(nums[i])
        index = absoluteValue-1
        if nums[index] < 0:
            continue
        else:
            nums[index] = -nums[index]
    disappearedNumber = []
    for i in range(n):
        if nums[i] >= 0:
            disappearedNumber.append(i+1)
    return disappearedNumber

result = findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(result)
