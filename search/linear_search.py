def linear_search(arr, arr_len, finding_element):
    for i in range(0, arr_len):
        if arr[i] == finding_element:
            return i
    return -1


arr = [5, 6, 8, 2, 6, 10, 7, 3]
finding_element = 6
arr_len = len(arr)

result = linear_search(arr, arr_len, finding_element)
if result != -1:
    print("Element is present at index :", str(result))
else:
    print("Element is not present in the array")
