import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = max_len = 0
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len

    def test_lengthOfLongestSubstring(self):
        test_cases = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
            ("a", 1),
            ("au", 2),
            ("dvdf", 3),
            ("abba", 2),
            ("tmmzuxt", 5),
            ("anviaj", 5),
            ("ohvhjdml", 6),
            ("abcdeafbdgcbb", 7),
            ("aab", 2),
            ("abcabcbb", 3),
            ("bpfbhmipx", 7),
            ("abcdefg", 7),
            ("aabbcc", 2),
            ("abcddefgh", 6),
            ("abba", 2),
            ("tmmzuxt", 5),
        ]
        passed = 0
        for idx, (s, expected) in enumerate(test_cases, 1):
            result = self.lengthOfLongestSubstring(s)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={s}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_lengthOfLongestSubstring()

if __name__ == "__main__":
    run_tests()
