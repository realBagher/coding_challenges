import unittest

from solution import Solution


class TestTwoSum(unittest.TestCase):
    def test_example_1(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_example_2(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([3, 2, 4], 6), [1, 2])

    def test_example_3(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([3, 3], 6), [0, 1])

    def test_example_4(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([3, 5, 4, 9], 7), [0, 2])

    def test_example_5(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([3, 2, 3, 4], 6), [0, 2])


if __name__ == "__main__":
    unittest.main()
