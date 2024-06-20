# Python program for Swap elements in String list
# Time Complexity: O(n)

list = ['Swap', 'elements', 'in', 'String', 'list']

newList = [sub.replace('s', '-')
           .replace('s', '$')
           .replace('-', '$')
           for sub in list]
print("List after replacing characters: " + str(newList))