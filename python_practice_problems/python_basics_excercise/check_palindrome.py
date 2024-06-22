# Palindrome is a word, phrase, or sequence that reads the same backwards as forwards.
# Write a function to check palindrome.

def is_palindrome(word):
    return word == word[::-1]


word = "madam"
print(is_palindrome(word))
