# Count number of words in a string.

from collections import defaultdict
from typing import Dict
import unittest


def solution(string: str) -> Dict[str, int]:
    word_count = defaultdict(int)
    sanitize_string = string.lower().split()
    for word in sanitize_string:
        word_count[word] += 1
    return word_count

class TestSolution(unittest.TestCase):
    def test_basic_case(self):
        input_string = """data engineering is a good skill to have
        # Data is the new oil
        # Data engineering can be massive"""

        expected_output = {
        'data': 3,
        'engineering': 2,
        'is': 2,
        'a': 1,
        'good': 1,
        'skill': 1,
        'to': 1,
        'have': 1,
        '#': 2,
        'the': 1,
        'new': 1,
        'oil': 1,
        'can': 1,
        'be': 1,
        'massive': 1
        }
        self.assertEqual(solution(input_string), expected_output)


if __name__ == "__main__":
    input_string = """data engineering is a good skill to have
# Data is the new oil
# Data engineering can be massive"""

    count = solution(string=input_string)
    print(count)

    unittest.main()