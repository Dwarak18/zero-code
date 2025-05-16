import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def isMatch(self, s, p):
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                ans = i == len(s)
            else:
                first = i < len(s) and p[j] in {s[i], '.'}
                if j+1 < len(p) and p[j+1] == '*':
                    ans = dp(i, j+2) or (first and dp(i+1, j))
                else:
                    ans = first and dp(i+1, j+1)
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)

    def test_isMatch(self):
        test_cases = [
            ("aa", "a", False),
            ("aa", "a*", True),
            ("ab", ".*", True),
            ("aab", "c*a*b", True),
            ("mississippi", "mis*is*p*.", False),
            ("", "", True),
            ("", ".*", True),
            ("a", "ab*", True),
            ("bbbba", ".*a*a", True),
            ("ab", ".*c", False),
            ("aaa", "a*a", True),
            ("aaa", "ab*a*c*a", True),
            ("a", "ab*a", False),
            ("a", "ab*a*", True),
            ("abcd", "d*", False),
            ("", "c*", True),
            ("a", "ab*", True),
            ("bbbba", ".*a*a", True),
            ("ab", ".*c", False),
            ("aaa", "a*a", True),
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
