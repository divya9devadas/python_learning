# Python program for Swap elements in String list
# Time Complexity: O(n)

list = ['Swap', 'elements', 'in', 'String', 'list']

newList = ", ".join(list)
newList = (newList.replace('S', '_')
           .replace('@', 'S')
           .replace('_', '@')
           .split(', '))

print("List after replacing characters: " + str(newList))