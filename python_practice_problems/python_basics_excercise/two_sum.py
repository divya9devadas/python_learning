def twoSum(nums, target):
    temp_dict = {}

    for ind in range(len(nums)):
        complement = target - nums[ind]
        if complement in temp_dict:
            return temp_dict[complement], ind
        temp_dict[nums[ind]] = ind


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
