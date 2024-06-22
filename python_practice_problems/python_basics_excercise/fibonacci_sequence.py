# Write a function to generate the first n numbers in the
# Fibonacci sequence [0, 1, 1, 2, 3, 5, 8, 13, 21, 34].

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence


n = 10
print(fibonacci(n))
