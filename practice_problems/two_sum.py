def twoSum(nums, target):
    temp_dict = {}

    for ind in range(len(nums)):
        complement = target - nums[ind]
        if complement in temp_dict:
            return temp_dict[complement], ind
        temp_dict[nums[ind]] = ind