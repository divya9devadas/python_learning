def calculate_median(nums):
    nums_sorted = sorted(nums)
    n = len(nums_sorted)
    if n % 2 == 0:
        return (nums_sorted[n // 2 - 1] + nums_sorted[n // 2]) / 2
    else:
        return nums_sorted[n // 2]


print(calculate_median([1, 2, 3, 4, 5]))
print(calculate_median([1, 2, 3, 4, 5, 6]))
print(calculate_median([10, 20, 30, 40, 50, 60]))
