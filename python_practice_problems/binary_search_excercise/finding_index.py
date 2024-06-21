# Search insert position of 'k' in a sorted array
# arr: The sorted array in which we need to find the position for K.
# n: The length of the array.
# K: The value we are searching for or need to insert.
# i: The index value

def find_index(arr, n, k):
    for i in range(n):

        if arr[i] == k:
            return i
        elif arr[i] > k:
            return i

    return n


arr = [1, 3, 5, 6]
n = len(arr)
k = 100
print(find_index(arr, n, k))
