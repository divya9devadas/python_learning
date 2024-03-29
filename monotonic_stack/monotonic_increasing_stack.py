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
            pos