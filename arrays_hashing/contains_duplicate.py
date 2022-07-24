import unittest
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False


class TestSolution(unittest.TestCase):

    def test_should_return_true1(self):
        nums = [1, 2, 3, 1]
        self.assertTrue(Solution().containsDuplicate(nums))

    def test_should_return_false(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(Solution().containsDuplicate(nums))

    def test_should_return_true2(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(Solution().containsDuplicate(nums))
