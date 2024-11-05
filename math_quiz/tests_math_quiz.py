import unittest
from math_quiz import randomNumber, randomOperator, compilesQuestion


class TestMathGame(unittest.TestCase):

    def test_randomNumber(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randomNumber(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_randomOperator(self):
        # TODO
        for _ in range(1000):
            operator = randomOperator()
            self.assertTrue(operator == "+" or operator == "-" or operator == "*")
        

    def test_compilesQuestion(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 8, '*', '5 * 8', 40),
                (5, 9, '-', '5 - 9', -4)

            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                PROBLEM, ANSWER = compilesQuestion(num1, num2, operator)
                self.assertTrue(PROBLEM == expected_problem and ANSWER == expected_answer)


if __name__ == "__main__":
    unittest.main()
