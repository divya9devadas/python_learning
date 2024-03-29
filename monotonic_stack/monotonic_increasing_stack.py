"""
Leetcode #739
"""
from typing import List


def solve_nested_loop(temperatures) -> List:
    """
    Using nested loop (non-optimal solution)
    """
    n = len(temperatures)
    answer = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if temperatures[j] > temperatures[i]:
                answer[i] = j - i
                break
    return answer


def solve(temperatures) -> List:
    """
    Using Monostack (optimal solution)
    """
    n = len(temperatures)
    answer = [0] * n
    stack = []
    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            pos = stack.pop()
            answer[pos] = i - pos
        stack.append(i)
    return answer


if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    print(solve(temperatures))
