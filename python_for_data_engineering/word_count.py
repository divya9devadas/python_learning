# Count number of words in a string.

from collections import defaultdict
from typing import Dict


def solution(string: str) -> Dict[str, int]:
    word_count = defaultdict(int)
    sanitize_string = string.lower().split()
    for word in sanitize_string:
        word_count[word] += 1
    return word_count


