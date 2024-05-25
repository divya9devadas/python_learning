def twoSum(nums, target):
    temp_dict = {}

    for ind in range(len(nums)):
        complement = target - nums[ind]