test_list = [4, 5, 6, 7, 3, 9]
a, b = 3, 10

result = any(a <= x < b for x in test_list)

print("Does list contain any element in range: " + str(result))