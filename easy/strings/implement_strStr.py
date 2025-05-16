import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

    def test_strStr(self):
        test_cases = [
            ("hello", "ll", 2),
            ("aaaaa", "bba", -1),
            ("", "", 0),
            ("a", "a", 0),
            ("a", "b", -1),
            ("mississippi", "issip", 4),
            ("mississippi", "issi", 1),
            ("mississippi", "mississippi", 0),
            ("mississippi", "mississippia", -1),
            ("abc", "c", 2),
            ("abc", "", 0),
            ("", "a", -1),
            ("needle", "needle", 0),
            ("needle", "le", 4),
            ("abcabcabc", "cab", 2),
            ("abcabcabc", "bca", 1),
            ("abcabcabc", "abc", 0),
            ("abcabcabc", "abcd", -1),
            ("abc", "abcabc", -1),
            ("abcabcabc", "cabc", 2),
        ]
        passed = 0
        for idx, (haystack, needle, expected) in enumerate(test_cases, 1):
            result = self.strStr(haystack, needle)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_strStr()

if __name__ == "__main__":
    run_tests()
