import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = dict()

        for letter in s:
            if letter in hashmap.keys():
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1

        for letter in t:
            if letter not in hashmap.keys():
                return False
            else:
                if hashmap[letter] <= 0:
                    return False
                else:
                    hashmap[letter] -= 1
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        """
        A bit worse solution
        """
        return sorted(s) == sorted(t)


class TestSolution(unittest.TestCase):

    def test_should_return_true(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(Solution().isAnagram2(s, t))

    def test_should_return_false(self):
        s = "rat"
        t = "car"
        self.assertFalse(Solution().isAnagram2(s, t))
