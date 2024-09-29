# count the average length of words in a set

import unittest
def avg_word_len(words: set) -> float:
    total_len = sum(len(word) for word in words)
    return total_len / len(words)


class TestAvgWordLen(unittest.TestCase):

    def test_basic_case(self):
        words_set = {"elephant", "tiger", "zebra", "giraffe", "monkey"}
        expected_result = (8 + 5 + 5 + 7 + 6) / 5  # manually calculated
        self.assertAlmostEqual(avg_word_len(words_set), expected_result)

    def test_single_word(self):
        words_set = {"elephant"}
        expected_result = 8
        self.assertEqual(avg_word_len(words_set), expected_result)


if __name__ == '__main__':
    words_set = {"elephant", "tiger", "zebra", "giraffe", "monkey"}

    solution = avg_word_len(words=words_set)
    print(solution)

    unittest.main()