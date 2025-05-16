import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or not s:
            return 0
        left = 0
        max_len = 0
        count = defaultdict(int)
        for right, char in enumerate(s):
            count[char] += 1
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

    def test_lengthOfLongestSubstringKDistinct(self):
        test_cases = [
            ("eceba", 2, 3),
            ("aa", 1, 2),
            ("a", 1, 1),
            ("", 1, 0),
            ("abcadcacacaca", 3, 10),
            ("abaccc", 2, 4),
            ("aabbcc", 1, 2),
            ("aabbcc", 2, 4),
            ("aabbcc", 3, 6),
            ("abcabcabc", 2, 2),
            ("abcabcabc", 3, 9),
            ("abc", 1, 1),
            ("abc", 2, 2),
            ("abc", 3, 3),
            ("aabbcc", 0, 0),
            ("aabbcc", 4, 6),
            ("aabbcc", 5, 6),
            ("aabbcc", 6, 6),
            ("aabbcc", 7, 6),
            ("aabbcc", 8, 6),
        ]
        passed = 0
        for idx, (s, k, expected) in enumerate(test_cases, 1):
            result = self.lengthOfLongestSubstringKDistinct(s, k)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({s}, {k}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_lengthOfLongestSubstringKDistinct()

if __name__ == "__main__":
    run_tests()
