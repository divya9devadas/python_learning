def is_balanced(parentheses):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in parentheses:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

# Test cases
print(is_balanced("()"))              # Expected output: True
print(is_balanced("{[()]()}"))        # Expected output: True
print(is_balanced("{[([)]}"))         # Expected output: False
print(is_balanced("({}[])"))