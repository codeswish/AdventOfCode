import unittest
import parser

# An opening parenthesis, (, means he should go up one floor (+1),
# and a closing parenthesis, ), means he should go down one floor (-1).


class TestParenCounter(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(parser.parse(""), 0, "Should be 0")

    def test_single_left_paren(self):
        self.assertEqual(parser.parse("("), 1, "Should be 1")

    def test_single_right_paren(self):
        self.assertEqual(parser.parse(")"), -1, "Should be -1")

    def test_multi_left_parens(self):
        self.assertEqual(parser.parse("(("), 2, "Should be 2")

    def test_parens(self):
        self.assertEqual(parser.parse("(())"), 0, "Should be 0")
        self.assertEqual(parser.parse("()()"), 0, "Should be 0")
        self.assertEqual(parser.parse("((("), 3, "Should be 3")
        self.assertEqual(parser.parse("(()(()("), 3, "Should be 3")
        self.assertEqual(parser.parse("())"), -1, "Should be -1")
        self.assertEqual(parser.parse("))("), -1, "Should be -1")
        self.assertEqual(parser.parse(")))"), -3, "Should be -3")
        self.assertEqual(parser.parse(")())())"), -3, "Should be -3")


if __name__ == "__main__":
    unittest.main()
