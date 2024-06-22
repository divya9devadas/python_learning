# Write a function to remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))


lst = [1, 4, 6, 3, 2, 4, 3, 1, 2, 3, 3]
print(remove_duplicates(lst))