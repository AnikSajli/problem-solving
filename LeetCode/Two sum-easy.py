def twoSum (nums, target):
    dictionary = dict()
    for i in range(0,len(nums)):
        number = nums[i]
        complement = target - nums[i]
        if complement not in dictionary:
            dictionary[number] = i
        else:
            print(i, dictionary[complement])

twoSum([3,3], 6)
