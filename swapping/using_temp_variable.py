# Python program to interchange first and last elements in a list

#  1) Finding the length of the list and
#  swapping the first element with Last element [i.e. (n-1)th]
def interchange(listA):
    size = len(listA)

    temp = listA[0]
    listA[0] = listA[size - 1]
    listA[size - 1] = temp

    return listA


listA = [12, 35, 9, 56, 24]
print(interchange(listA))


# 2) Swapping list[0] with list[-1]
# The last element is referred as list[-1]
# Time Complexity: O(1)

def swap_list(listB):
    listB[0], listB[-1] = listB[-1], listB[0]

    return listB


listB = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(swap_list(listB))
