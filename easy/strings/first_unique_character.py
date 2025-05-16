import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1

    def test_first_uniq_char(self):
        test_cases = [
            ("leetcode", 0),
            ("loveleetcode", 2),
            ("aabb", -1),
            ("", -1),
            ("a", 0),
            ("abcabc", -1),
            ("abcde", 0),
            ("aabbccdde", 8),
            ("aabbccddeeffg", 12),
            ("z", 0),
            ("zz", -1),
            ("abcabcabc", -1),
            ("aabbccddeeff", -1),
            ("aabbccddeeffggh", 14),
            ("aabbccddeeffgghh", -1),
            ("abc", 0),
            ("aab", 2),
            ("aabbc", 4),
            ("aabbcc", -1),
            ("abcdabcd", -1),
        ]
        passed = 0
        for idx, (s, expected) in enumerate(test_cases, 1):
            result = self.firstUniqChar(s)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_first_uniq_char()

if __name__ == "__main__":
    run_tests()
