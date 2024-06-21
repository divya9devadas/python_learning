def sqrt(num):
    if num == 0 or num == 1:
        return num

    i = 1
    result = 1
    while result <= num:
        i += 1
        result = i * i

    return i - 1


num = 11
sqrt_num = sqrt(num)
print(f"Square-root of {num} is approximately {sqrt_num}")
