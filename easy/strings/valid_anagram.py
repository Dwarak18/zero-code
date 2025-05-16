import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def test_is_anagram(self):
        test_cases = [
            ("anagram", "nagaram", True),
            ("rat", "car", False),
            ("", "", True),
            ("a", "a", True),
            ("a", "b", False),
            ("abc", "cba", True),
            ("abc", "ab", False),
            ("listen", "silent", True),
            ("triangle", "integral", True),
            ("apple", "papel", True),
            ("apple", "pale", False),
            ("abcd", "dcba", True),
            ("abcd", "abce", False),
            ("aabbcc", "baccab", True),
            ("aabbcc", "aabbc", False),
            ("abcabc", "cbacba", True),
            ("abcabc", "cbacbb", False),
            ("aabb", "bbaa", True),
            ("aabb", "bbaaa", False),
            ("", "a", False),
        ]
        passed = 0
        for idx, (s, t, expected) in enumerate(test_cases, 1):
            result = self.isAnagram(s, t)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_is_anagram()

if __name__ == "__main__":
    run_tests()
