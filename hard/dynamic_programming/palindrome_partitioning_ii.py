import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def minCut(self, s):
        n = len(s)
        dp = [i for i in range(n)]
        is_pal = [[False]*n for _ in range(n)]
        for end in range(n):
            for start in range(end+1):
                if s[start] == s[end] and (end-start<=1 or is_pal[start+1][end-1]):
                    is_pal[start][end] = True
                    if start == 0:
                        dp[end] = 0
                    else:
                        dp[end] = min(dp[end], dp[start-1]+1)
        return dp[-1] if n else 0

    def test_minCut(self):
        test_cases = [
            ("aab", 1),
            ("a", 0),
            ("ab", 1),
            ("aabb", 1),
            ("aabbaa", 0),
            ("racecar", 0),
            ("banana", 1),
            ("cdd", 1),
            ("cbbbcc", 1),
            ("aabbc", 2),
            ("aabbcc", 2),
            ("aabbccd", 3),
            ("aabbccdd", 4),
            ("aabbccdde", 5),
            ("aabbccddeeff", 6),
            ("aabbccddeeffg", 7),
            ("aabbccddeeffgg", 7),
            ("aabbccddeeffggh", 8),
            ("aabbccddeeffgghh", 8),
            ("aabbccddeeffgghhi", 9),
        ]
        passed = 0
        for idx, (s, expected) in enumerate(test_cases, 1):
            result = self.minCut(s)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={s}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_minCut()

if __name__ == "__main__":
    run_tests()
