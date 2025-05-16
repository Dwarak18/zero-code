import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def isInterleave(self, s1, s2, s3):
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0:
                    dp[i][j] |= dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                if j > 0:
                    dp[i][j] |= dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
        return dp[m][n]

    def test_isInterleave(self):
        test_cases = [
            ("aabcc", "dbbca", "aadbbcbcac", True),
            ("aabcc", "dbbca", "aadbbbaccc", False),
            ("", "", "", True),
            ("", "", "a", False),
            ("a", "", "a", True),
            ("", "a", "a", True),
            ("a", "b", "ab", True),
            ("a", "b", "ba", True),
            ("a", "b", "aa", False),
            ("a", "b", "bb", False),
            ("abc", "def", "adbcef", True),
            ("abc", "def", "abdecf", True),
            ("abc", "def", "abcdef", True),
            ("abc", "def", "defabc", True),
            ("abc", "def", "abcfde", False),
            ("abc", "def", "abdefc", False),
            ("abc", "def", "dabecf", False),
            ("abc", "def", "abdecf", True),
            ("abc", "def", "abdecf", True),
            ("abc", "def", "abdecf", True),
        ]
        passed = 0
        for idx, (s1, s2, s3, expected) in enumerate(test_cases, 1):
            result = self.isInterleave(s1, s2, s3)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({s1}, {s2}, {s3}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_isInterleave()

if __name__ == "__main__":
    run_tests()
