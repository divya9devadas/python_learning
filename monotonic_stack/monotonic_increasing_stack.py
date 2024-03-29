"""
Leetcode #739
"""
from typing import List


def solve(temperatures) -> List:
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
