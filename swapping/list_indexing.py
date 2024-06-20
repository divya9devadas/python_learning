# Python program to interchange first and last elements in a list

# The last element is referred as list[-1]
# Time Complexity: O(1)

def interchange(listA):
    listA[0], listA[-1] = listA[-1], listA[0]

    return listA


listA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(interchange(listA))


# Python Program to Swap Two Elements in a List

def swap_list(listB, pos1, pos2):

    listB[pos1], listB[pos2] = listB[pos2], listB[pos1]
    return listB


listB = [23, 56, 78, 14, 90, 7, 31]
pos1, pos2 = 1, 5
print(swap_list(listB, pos1-1, pos2-1))
