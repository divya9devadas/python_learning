# Write a Python function that takes a list of integers and
# returns a new list with only the unique elements,
# preserving the order of their first occurrence.

def unique_elements(list):
    seen = set()
    unique_list = []