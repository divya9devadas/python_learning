# Count number of words in a string.

from collections import defaultdict
from typing import Dict
import unittest


# 1. Given a sentence, count the distinct words in the sentence
def word_count(string: str) -> int:
    return len(set(string.split()))

# 2. Given a sentence, count the distinct words in the sentence, use a Dictionary.
def word_count_dic(string: str) -> Dict[str, int]:
    sanitize_string = string.lower().split()
    count_dic = defaultdict(int)
    for word in sanitize_string:
        count_dic[word] += 1
    return count_dic


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

    def test_case_insensitivity(self):
        input_string = "Data data DATA"
        expected_output = {'data': 3}
        self.assertEqual(solution(input_string), expected_output)

    def test_punctuations(self):
        input_string = "and, ball! world."
        expected_output = {'and,': 1, 'ball!': 1, 'world.': 1}
        self.assertEqual(solution(input_string), expected_output)

    def test_multiple_spaces(self):
        input_string = "   data    data   "
        expected_output = {'data': 2}
        self.assertEqual(solution(input_string), expected_output)


if __name__ == "__main__":
    input_string = """data engineering is a good skill to have
# Data is the new oil
# Data engineering can be massive"""

    solution1 = word_count(string=input_string)
    solution2 = word_count_dic(string=input_string)

    print(f"Total length of the string: {solution1}")
    print(f"Distinct word count: {solution2}")

    unittest.main()
