def product(value):
    result = 1
    for ele in value:
        result *= ele
    return result


test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))

result = []
[result.append(i) for i in test_list if i not in result]
result = product(result)

print("List product excluding duplicates : " + str(result))