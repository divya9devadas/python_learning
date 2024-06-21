def containsDuplicate(nums):
    num_dict = set()
    for num in nums:
        if num in num_dict:
            return True
        else:
            num_dict.add(num)
    return False


nums = [1, 2, 3, 1]
print(containsDuplicate(nums))
