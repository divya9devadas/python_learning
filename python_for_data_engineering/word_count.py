# Count number of words in a string.

from collections import defaultdict
from typing import Dict


def solution(string: str) -> Dict[str, int]:
    word_count = defaultdict(int)
    sanitize_string = string.lower().split()
    for word in sanitize_string:
        word_count[word] += 1
    return word_count


if __name__ == "__main__":
    input_string = """data engineering is a good skill to have
# Data is the new oil
# Data engineering can be massive"""
    count = solution(string=input_string)
    print(count)