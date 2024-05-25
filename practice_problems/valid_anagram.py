def isAnagram(k, l):
    k_counter = {}
    l_counter = {}

    for letter in k:
        if letter not in k_counter:
            k_counter[letter] = 0
        k_counter[letter] = k_counter[letter] + 1

    for letter in l:
        if letter not in l_counter:
            l_counter[letter] = 0
        l_counter[letter] = l_counter[letter] + 1
    return k_counter == l_counter