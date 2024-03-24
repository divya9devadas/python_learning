# Finding element from a sorted array

def binary_iterative_search(arr, finding_element):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < finding_element:
            low = mid + 1
        elif arr[mid] > finding_element:
            high = mid - 1
        else:
            return mid
    return -1


arr = [1, 3, 5, 7, 8, 12, 14, 15, 17, 19, 28, 55]
finding_element = 15

result = binary_iterative_search(arr, finding_element)
if result != -1:
    print("Element present at index :", str(result))
else:
    print("Element is not present in the array")
