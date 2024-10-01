from collections import defaultdict


def unique_values(arr1:list, arr2:list) -> list:
    result = []
    count = defaultdict(int)
    for word in arr1:  # run m times
        count[word] += 1
    print(count)
    for word in arr2:  # run n times
        count[word] += 1
    print(count)
    for key in count: # run m+n times
        if count[key] == 1:
            result.append(key)
    return result

"""
Time Complexity(m+n+m+n)= 2m+2n: O(m+n)
Space Complexity: m+n

"""

if __name__ == "__main__":
     array1 = ["this", "is", "my", "test"] # length is m
     array2 = ["this", "is", "my", "array", "dad"] # length is n
     solution = unique_values(arr1=array1,arr2=array2)
     print(solution)
