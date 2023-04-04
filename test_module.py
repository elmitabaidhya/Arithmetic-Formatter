import unittest
from arithmetic_arranger import arithmetic_arranger


# Test cases
class UnitTests(unittest.TestCase):

  def test_arrangement(self):
    actual = arithmetic_arranger(
      ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    expected = "   32      3801      45      123\n+ 698    -    2    + 43    +  49\n-----    ------    ----    -----"
    self.assertEqual(
      actual, expected,
      'Expected different output when calling "arithmetic_arranger()" with ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]'
    )

    actual = arithmetic_arranger(
      ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
    expected = "  32         1      9999      523\n+  8    - 3801    + 9999    -  49\n----    ------    ------    -----"
    self.assertEqual(
      actual, expected,
      'Expected different output when calling "arithmetic_arranger()" with ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]'
    )

  def test_too_many_problems(self):
    actual = arithmetic_arranger([
      "32 + 698", "3801 - 2", "45 + 43", "123 + 49", "32 + 8", "1 - 3801",
      "9999 + 9999", "523 - 49"
    ])
    expected = "Error: Too many problems."
    self.assertEqual(
      actual, expected,
      'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."'
    )

  def test_incorrect_operator(self):
    actual = arithmetic_arranger(
      ["32 + 8", "1 * 3801", "9999 + 9999", "523 / 49"])
    expected = "Error: Operator must be '+' or '-'."
    self.assertEqual(
      actual, expected,
      '''Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return "Error: Operator must be '+' or '-'."'''
    )

  def test_too_many_digits(self):
    actual = arithmetic_arranger(
      ["32 + 8", "1 - 38001", "9999 + 99991", "523 - 49"])
    expected = "Error: Numbers cannot be more than four digits."
    self.assertEqual(
      actual, expected,
      'Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to return "Error: Numbers cannot be more than four digits."'
    )

  def test_only_digits(self):
    actual = arithmetic_arranger(
      ["32 + 698", "3801 - 2a", "45 + 43", "123 + 49"])
    expected = "Error: Numbers must only contain digits."
    self.assertEqual(
      actual, expected,
      'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."'
    )

  def test_solutions(self):
    actual = arithmetic_arranger(
      ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
    expected = "  32         1      9999      523\n+  8    - 3801    + 9999    -  49\n----    ------    ------    -----\n  40     -3800     19998      474"
    self.assertEqual(
      actual, expected,
      'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with arithmetic problems and a second argument of `True`.'
    )


if __name__ == "__main__":
  unittest.main()
