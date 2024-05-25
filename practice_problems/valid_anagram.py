def isAnagram(k, l):
    k_counter = {}
    l_counter = {}

    for letter in k:
        if letter in k_counter:
            k_counter[letter] = 0
        k_counter[letter] = k_counter[letter] + 1
