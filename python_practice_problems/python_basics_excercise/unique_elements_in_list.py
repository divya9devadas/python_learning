# Write a Python function that takes a list of integers and
# returns a new list with only the unique elements,
# preserving the order of their first occurrence.

def unique_elements(list):
    seen = set()
    unique_list = []
    for i in list:
        if i not in seen:
            seen.add(i)
            unique_list.append(i)
    return unique_list

num = [1,3,4,2,6,3,5,1,7,2,8,3,9,4,9,6]
print(f'List with unique elements')