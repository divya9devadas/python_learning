# Python program to interchange first and last elements in a list

#  Finding the length of the list and
#  swapping the first element with Last element [i.e. (n-1)th]
def interchange(listA):
    size = len(listA)

    temp = listA[0]
    listA[0] = listA[size - 1]
    listA[size - 1] = temp

    return listA


listA = [12, 35, 9, 56, 24]
print(interchange(listA))


def swap_list(listB, pos1, pos2):
    temp = listB[pos1]
    listB[pos1] = listB[pos2]
    listB[pos2] = temp

    return listB


listB = [89, 24, 56, 12, 5]
pos1, pos2 = 2, 5
print(swap_list(listB, pos1-1, pos2-1))
