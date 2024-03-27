def reverse_string(text):
    stack = []

    for elm in text:
        stack.append(elm)
    reversed_text = ""

    while stack:
        reversed_text += stack.pop()
    print(reversed_text, text)


text = "hello"

reverse_string(text)