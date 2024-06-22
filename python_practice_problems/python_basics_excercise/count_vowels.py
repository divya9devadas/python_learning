# Write a function to count the number of vowels in a given string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


s = "Able was I ere I saw Elba"
print(count_vowels(s))
