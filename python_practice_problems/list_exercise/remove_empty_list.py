# Python program for removing empty lists from a list

def remove_empty_lists(list):
    return [elem for elem in list if elem]


list = [5, 6, [], 3, [], [], 9]
print("Removed empty list: " + str(remove_empty_lists(list)))
