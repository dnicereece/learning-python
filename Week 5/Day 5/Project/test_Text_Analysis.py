# Create a test module to test functions from project programs
# Import the unit test module
import unittest
# Import functions to be tested (from the Text_Analysis.py file)
from Text_Analysis import word_count, character_count, uppercase_conversion, lowercase_conversion, title_case_conversion, sentence_count, average_reading_level, most_common_word
# Define a test class that inherits from unittest.TestCase
class TestTextAnalysis(unittest.TestCase):
    # Test for word_count function
    def test_word_count(self):
        self.assertEqual(word_count("Hello world!"), 2)
    # Test for character_count function
    def test_character_count(self):
        self.assertEqual(character_count("Hello"), 5)
    # Test for uppercase_conversion function
    def test_uppercase_conversion(self):
        self.assertEqual(uppercase_conversion("hello"), "HELLO")
    # Test for lowercase_conversion function
    def test_lowercase_conversion(self):
        self.assertEqual(lowercase_conversion("HELLO"), "hello")
    # Test for title_case_conversion function
    def test_title_case_conversion(self):
        self.assertEqual(title_case_conversion("hello world"), "Hello World")
    # Test for sentence_count function
    def test_sentence_count(self):
        self.assertEqual(sentence_count("Hello world! This is a test."), 2)
    # Test for average_reading_level function
    def test_average_reading_level(self):
        self.assertAlmostEqual(average_reading_level("The quick brown fox jumped over the lazy dog. The quick brown fox jumped over the lazy dog."), 84.9, places=1)
    # Test for most_common_words function
    def test_most_common_word(self):
        self.assertEqual(most_common_word("apple banana apple orange banana apple", n=2), "apple")
# Run the tests
if __name__ == '__main__':
    unittest.main()