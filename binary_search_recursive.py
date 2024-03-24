# Finding an element from a sorted list

def binary_recursive_search(arr, low, high, finding_element):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == finding_element:
            return mid
        elif arr[mid] > finding_element:
            return binary_recursive_search(arr, low, mid-1, finding_element)
        else:
            return binary_recursive_search(arr, mid+1, high, finding_element)
    else:
        return -1


arr = [4, 7, 9, 12, 15, 18, 20, 35, 48]
finding_element = 18

result = binary_recursive_search(arr, 0, len(arr) - 1, finding_element)
if result != -1:
    print("Element is present at index :", str(result))
else:
    print("Element is not present in the array")
