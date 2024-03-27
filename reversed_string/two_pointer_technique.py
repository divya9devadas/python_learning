def reverse_string(text):
    l = 0
    r = len(text) - 1

    while l < r:
        left = text[l]
        right = text[r]
        text[l], text[r] = right, left
        l = l + 1
        r = r - 1
    return text


text = list("Hello World")
print(reverse_string(text))
