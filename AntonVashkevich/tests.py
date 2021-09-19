import unittest
from task_1 import replace_quotes
from task_2 import is_palindrome
from task_3 import my_split
from task_4 import split_by_index
from task_5 import get_digits
from task_6 import get_longest_word
from task_7 import product_of_items
from task_8 import get_pairs
from task_9 import check_all, check_one, check_two, check_alphabet
from task_10 import generate_squares
from task_11 import combine_dicts


class TestHomework(unittest.TestCase):
    # Task 1
    def test_replace_quotes(self):
        self.assertEqual(replace_quotes("\'\"\'\""), "\"\'\"\'")

    # Task 2
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("91019"))
        self.assertTrue(is_palindrome("Anna"))
        self.assertFalse(is_palindrome("assert false"))
        self.assertTrue(is_palindrome("A lot not new I saw as I went on to L.A."))

    # Task 3
    def test_my_split(self):
        test_string = "Hello world python"
        self.assertListEqual(my_split(test_string), test_string.split())
        self.assertListEqual(my_split(test_string, ","), test_string.split(","))
        self.assertListEqual(my_split(test_string, "world"), test_string.split("world"))
        self.assertListEqual(my_split(test_string, "l"), test_string.split("l"))

    # Task 4
    def test_split_by_index(self):
        self.assertListEqual(split_by_index("pythoniscool,isn'tit?",
                                            [6, 8, 12, 13, 18]),
                                            ["python", "is", "cool", ",", "isn't", "it?"],
                             )
        self.assertListEqual(split_by_index("no luck", [42]), ['no luck'])

    # Task 5
    def test_get_digits(self):
        self.assertTupleEqual(get_digits(87178291199), (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9))
        self.assertTupleEqual(get_digits(1234), (1, 2, 3, 4))

    # Task 6
    def test_get_longest_word(self):
        self.assertEqual(get_longest_word("Python is simple and effective!"), "effective!")
        self.assertEqual(get_longest_word("Any pythonista like namespaces a lot."), "pythonista")
        self.assertEqual(get_longest_word("same!! length return"), "same!!")

    # Task 7
    def test_product_of_items(self):
        self.assertListEqual(product_of_items([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertListEqual(product_of_items([3, 2, 1]), [2, 3, 6])
        self.assertListEqual(product_of_items([1, 2]), [2, 1])

    # Task 8
    def test_get_pairs(self):
        self.assertListEqual(get_pairs([1, 2, 3, 8, 9]), [(1, 2), (2, 3), (3, 8), (8, 9)])
        self.assertListEqual(get_pairs(['need', 'to', 'sleep', 'more']),
                                        [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')])
        self.assertIsNone(get_pairs([1]), None)

    # Task 9
    def test_set(self):
        test_strings = ["hello", "world", "python", ]
        self.assertSetEqual(check_all(*test_strings), {'o'})
        self.assertSetEqual(check_one(*test_strings), {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'})
        self.assertSetEqual(check_two(*test_strings), {'h', 'l', 'o'})
        self.assertSetEqual(check_alphabet(*test_strings),
                            {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'})

    # Task 10
    def test_generate_squares(self):
        self.assertDictEqual(generate_squares(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})

    # Task 11
    def test_combine_dicts(self):
        dict_1 = {'a': 100, 'b': 200}
        dict_2 = {'a': 200, 'c': 300}
        dict_3 = {'a': 300, 'd': 100}
        self.assertDictEqual(combine_dicts(dict_1, dict_2), {'a': 300, 'b': 200, 'c': 300})
        self.assertDictEqual(combine_dicts(dict_1, dict_2, dict_3), {'a': 600, 'b': 200, 'c': 300, 'd': 100})


if __name__ == "__main__":
    unittest.main()
