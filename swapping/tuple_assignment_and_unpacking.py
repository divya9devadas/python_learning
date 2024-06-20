# Python program to swap first
# and last element of a list


def swap_list(list):
    get = list[0], list[-1]
    list[0], list[-1] = get

    return list


list = [12, 35, 9, 56, 24]
print(swap_list(list))


def swapList(list, pos1, pos2):
    get = list[pos1], list[pos2]

    list[pos2], list[pos1] = get

    return list


list = [4, 2, 6, 1, 9]
pos1, pos2 = 1, 3
print(swapList(list, pos1 - 1, pos2 - 1))
