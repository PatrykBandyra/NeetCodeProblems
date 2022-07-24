import unittest
from typing import List


class Solution:
    """
    Each input has exactly 1 solution.
    Not allowed to use the same element twice.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if num in hashmap.keys():
                return [i, hashmap[num]]
            else:
                hashmap[diff] = i


class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertListEqual(sorted(Solution().twoSum(nums, target)), sorted(expected))

    def test_2(self):
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        self.assertListEqual(sorted(Solution().twoSum(nums, target)), sorted(expected))

    def test_3(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertListEqual(sorted(Solution().twoSum(nums, target)), sorted(expected))
