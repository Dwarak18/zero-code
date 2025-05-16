import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        dict_t = Counter(t)
        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            while l <= r and formed == required:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]

    def test_minWindow(self):
        test_cases = [
            ("ADOBECODEBANC", "ABC", "BANC"),
            ("a", "a", "a"),
            ("a", "aa", ""),
            ("a", "b", ""),
            ("ab", "b", "b"),
            ("ab", "a", "a"),
            ("ab", "ab", "ab"),
            ("ab", "ba", "ab"),
            ("abc", "cba", "abc"),
            ("abc", "cab", "abc"),
            ("abc", "bac", "abc"),
            ("abc", "acb", "abc"),
            ("abc", "bca", "abc"),
            ("abc", "c", "c"),
            ("abc", "b", "b"),
            ("abc", "a", "a"),
            ("abc", "d", ""),
            ("abc", "abcd", ""),
            ("abc", "abc", "abc"),
            ("abc", "cba", "abc"),
        ]
        passed = 0
        for idx, (s, t, expected) in enumerate(test_cases, 1):
            result = self.minWindow(s, t)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({s}, {t}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_minWindow()

if __name__ == "__main__":
    run_tests()
