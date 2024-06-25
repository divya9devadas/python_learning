def calculate_median(nums):
    nums_sorted = sorted(nums)
    n = len(nums_sorted)
    if n % 2 == 0:
        return (nums_sorted[n // 2 - 1] + nums_sorted[n // 2]) / 2
    else:
        return nums_sorted[n // 2]

