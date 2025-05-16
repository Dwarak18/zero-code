import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]

    def test_isMatch(self):
        test_cases = [
            ("aa", "a", False),
            ("aa", "*", True),
            ("cb", "?a", False),
            ("adceb", "*a*b", True),
            ("acdcb", "a*c?b", False),
            ("", "*", True),
            ("", "", True),
            ("a", "?", True),
            ("a", "*?", True),
            ("a", "a*", True),
            ("a", "b*", False),
            ("abcde", "a*e", True),
            ("abcde", "a*d", False),
            ("abcde", "*?*?*?*?*", True),
            ("abcde", "*?*?*?*?*?*", False),
            ("abc", "*", True),
            ("abc", "a*", True),
            ("abc", "*c", True),
            ("abc", "*b*", True),
            ("abc", "*d*", False),
        ]
        passed = 0
        for idx, (s, p, expected) in enumerate(test_cases, 1):
            result = self.isMatch(s, p)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({s}, {p}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_isMatch()

if __name__ == "__main__":
    run_tests()
